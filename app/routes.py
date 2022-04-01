from app import app, forms
from flask import redirect, render_template, url_for, flash
# # from flask_login import login
from app.forms import SignUpForm
from app.models import User


@app.route('/')
def index():
	title = 'Home'
	user = {'id': 1, 'username': 'spowell', 'email': 'spowell@codingtemple.com'}
	posts = [
			{'id': 1, 
			'title': 'March', 
			'body': 'I hate march'}, 
			]
	return render_template('index.html', current_user=user, title=title, posts=posts)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    title = 'Sign Up'
    form = SignUpForm()
    # check if a post request and that the form is valid
    if form.validate_on_submit():
        # Get data from the validated form
        email = form.email.data
        username = form.username.data
        password = form.password.data
        # Create a new user instance with form data
        new_user = User(email=email, username=username, password=password)
        return redirect(url_for('index'))

    return render_template('signup.html', title=title, form=form)