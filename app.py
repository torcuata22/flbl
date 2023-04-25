from flask import Flask, render_template

#Create Flask Instance:
app = Flask(__name__)

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