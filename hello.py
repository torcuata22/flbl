from flask import Flask, render_template

#create flask instance:

 
app = Flask(__name__)
   
    
   

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

#set environmental variables ( in terminal):
#export FLASK_ENV=development, this is deprecated, try FLASK_DEBUG
#tell the server where the app "lives":
#export FLASK_APP=hello.py
#then, run the server: flask run

if __name__ == '__main__':
    app.run(debug=True)
