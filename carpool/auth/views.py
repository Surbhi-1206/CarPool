from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask_login import login_required, logout_user, login_user, current_user, LoginManager, login_manager
from carpool import app
from carpool.auth.AuthService import AuthService, UserExistsException, InvalidUserException
from carpool.auth.UserDto import UserDto
from .forms import SignUpForm, SignInForm
from carpool import models, db

a = Blueprint('auth', __name__, url_prefix='/auth')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'signin'


@login_manager.user_loader
def load_user(email):
    return models.Users.query.filter_by(email=email).first()


@app.before_request
def before_request():
    g.user = current_user


@a.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    handles new user sign up
    """
    print("In signup.....")
    auth_service = AuthService()
    form = SignUpForm()
    if request.method == 'GET':
        return render_template('auth/signup.html', title='Sign Up', form=form)

    elif request.method == 'POST':
        if form.validate_on_submit():
            user_dto = UserDto(form.email.data, form.password.data, form.name.data, form.contact.data)
            try:
                auth_service.create_user(user_dto)
                flash('SignUp successfull name = "%s" , email = "%s"' % (form.name.data, form.email.data))
                return redirect(url_for('auth.signin'))
            except UserExistsException:
                flash("User already exists")
                return redirect(url_for('auth.signup'))
        flash('SignUp Failed')
        return render_template('auth/signup.html', title='Sign Up', form=form)


@a.route('/signin', methods=['GET', 'POST'])
def signin():
    """
    handles existing user login
    """
    auth_service = AuthService()
    form = SignInForm()
    if request.method == 'GET':
        return render_template('auth/signin.html', title='Sign In', form=form)

    elif request.method == 'POST':
        if form.validate_on_submit():
            user_dto = UserDto(form.email.data)
            try:
                user = auth_service.load_user(user_dto)
                if user.password == form.password.data:
                    flash("Logged in successfully")
                    login_user(user)
                    return redirect(url_for('home.welcome'))
                else:
                    flash("Incorrect password")
                    return redirect(url_for('auth.signin'))
            except InvalidUserException:
                return ("User does not exist")
        flash('SignIn failed')
        return render_template('auth/signin.html', title='Sign In', form=form)


@a.route('/signout')
@login_required
def signout():
    """
    logout the current user
    """
    logout_user()
    flash('Logged Out Successfully')
    return redirect(url_for('home.welcome'))
