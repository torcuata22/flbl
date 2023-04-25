from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy


#Create Flask Instance:
app = Flask(__name__)

#Secret key (csrf token for forms):
app.config['SECRET_KEY']="this is my secret key"

#Create Form Class:
class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit =SubmitField("Submit")



#Routes:
@app.route('/')
def index():
    first_name="Loki"
    favorite_food="Tuna"
    favorite_toys=["Stumpy", "my Bumble Bee", "Mousy", "The hallway rug"]
    favorite_sound="Squeak!"
    return render_template('index.html', first_name=first_name, favorite_food=favorite_food,favorite_toys=favorite_toys, favorite_sound=favorite_sound)

@app.route('/user/<name>/')
def user(name):
    return render_template("user.html", name=name)

@app.route('/name', methods=['GET','POST'])
def name():
    name = None
    form = NamerForm()
    #validation:
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
        flash('Form submitted successfully!')
    return render_template('name.html', 
                           name=name, 
                           form=form,)

#custom error pages
@app.errorhandler(404)
def page_not_founr(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_founr(e):
    return render_template("500.html"), 500



#in Terminal: 
#export FLASK_ENV=development
#export FLASK_APP=app.py
#THEN: flask run