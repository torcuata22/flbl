from flask import Flask, render_template, flash, request #flash messages on the screen
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate


#create flask instance:
app = Flask(__name__)
#add Database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

#New MySQL DB:
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name' to switch, uncomment this and comment the other one
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pa55w0rd123@localhost/our_users'
#Create secret key:
app.config['SECRET_KEY']="m45u93r53cr37llav3"
db = SQLAlchemy(app)
migrate = Migrate(app,db)


#Create a model:
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True) #only one person per email address
    favorite_color = db.Column(db.String(120))
    data_added = db.Column(db.DateTime, default=datetime.utcnow)

#create a string:
    def __repr__(self):
        return '<Name %r>' % self.name
    
# Creation of the database tables within the application context.
with app.app_context():
    db.create_all()

class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    favorite_color=StringField("Favorite color")
    submit = SubmitField("Submit")
    
@app.route('/user_add/', methods=['GET','POST'])
def add_user():
    name=None
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(name=form.name.data, email=form.email.data, favorite_color=form.favorite_color.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = '' #clears the form
        form.email.data = '' #clears the form
        form.favorite_color.data = ''
        flash("User Added Successfully!")
    our_users = User.query.order_by(User.data_added)
    return render_template("add_user.html", form=form, name=name, our_users=our_users)
#need to create database form terminal: type python to enter interactive shell
#from hello(file name) import db
#db.create_all()this didn't work, so I did it on hello.py

#Create Form Class:
class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

#create a route (using decorator)
@app.route('/')
def index():
    first_name = "Loki"
    stuff = "This is <b>bold</b> text "
    favorite_pizza = ["Mushrooms", "Hawaiian","Cheese", "Peppers", 32]
    return render_template("index.html", 
                           first_name = first_name, 
                           stuff=stuff, 
                           favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", username=name) #"username" comes from func argument

#Custom error pages
#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

#create name page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    #Validate form:
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = '' #clears the form
        flash("Form submitted Successfully!")

    return render_template('name.html',name=name,form=form)

#Update DB record:
@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    form = UserForm()
    name_to_update = User.query.get_or_404(id)
    if request.method == 'POST':
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        name_to_update.favorite_color = request.form['favorite_color']

        try:
            db.session.commit()
            flash("User updated successfully")
            return render_template("update.html", 
                                   form=form,
                                   name_to_update=name_to_update)
        except:
            flash("Update failed, please try again")
            return render_template("update.html", 
                                   form=form,
                                   name_to_update=name_to_update)
    else:
        return render_template("update.html", 
                                   form=form,
                                   name_to_update=name_to_update)







#set environmental variables ( in terminal):
#export FLASK_ENV=development, this is deprecated, try FLASK_DEBUG
#tell the server where the app "lives":
#export FLASK_APP=hello.py
#then, run the server: flask run

if __name__ == '__main__':
    app.run(debug=True)


#to set up migrations:
#pip install Flask-Migrate
#make imports
#run: flask db init to create the directory that will hold the migrations (had to change name to app.py)
#first migration: flask db migrate -m "first migration", THEN flask db upgrade
