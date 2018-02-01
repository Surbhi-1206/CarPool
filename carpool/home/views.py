from flask import Blueprint , request , render_template , flash , g , session , redirect , url_for

h = Blueprint('home' , __name__ , url_prefix = '/home')

@h.route('/')
def welcome():
    print("rendering the welcome page")
    print("making a change in develop branch")
    return render_template('home/home.html')