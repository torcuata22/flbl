from flask import Flask, render_template

#create flask instance:
app = Flask(__name__)


'''
FILTERS:
safe --> to pass html (stop jinja from stripping it)
capitalize --> capitalizes first word
lower --> all lower case
upper -->ALL CAPS
title --> title case
trim --> removes trailing spaces from the end
striptags--> removes html tags
'''

#create a route (using decorator)
@app.route('/')
def index():
    first_name = "Loki"
    stuff = "This is <b>bold</b> text "
    favorite_pizza=["Mushrooms", "Hawaiian", "Perppers", "Cheese", 32]
    return render_template("index.html", 
                           first_name = first_name, 
                           stuff=stuff, 
                           favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", username=name) #"username" comes from func argument

#NEXT: https://www.youtube.com/watch?v=4yaG-jFfePc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz&index=2

#set environmental variables ( in terminal):
#export FLASK_ENV=development, this is deprecated, try FLASK_DEBUG
#tell the server where the app "lives":
#export FLASK_APP=hello.py
#then, run the server: flask run

if __name__ == '__main__':
    app.run(debug=True)
