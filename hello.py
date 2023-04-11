from flask import Flask, render_template

#create flask instance:
app = Flask(__name__)

#create a route (using decorator)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<name>')
def user(name):
    return "<h1>Hello {}</h1>".format(name)

#NEXT: https://www.youtube.com/watch?v=4yaG-jFfePc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz&index=2

#set environmental variables ( in terminal):
#export FLASK_ENV=development, this is deprecated, try FLASK_DEBUG
#tell the server where the app "lives":
#export FLASK_APP=hello.py
#then, run the server: flask run