from flask import Flask, render_template

#Create Flask Instance:
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#in Terminal: 
#export FLASK_ENV=development
#export FLASK_APP=app.py
#THEN: flask run