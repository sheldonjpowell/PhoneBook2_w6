from app import app, forms
from flask import redirect, render_template, url_for, flash
# # from flask_login import login
from app.forms import SignUpForm, AddressForm
from app.models import User, Address


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
    if form.validate_on_submit():

        username = form.username.data
        email = form.email.data
        password = form.password.data

        users_with_that_info = User.query.filter((User.username==username)|(User.email==email)).all()
        if users_with_that_info:
            flash(f"There is already a username and/or email", "danger")
            return redirect(url_for('signup'))
            
        new_user = User(username=username, email=email, password=password)

        flash(f"{new_user.username} has succesfully signed up.", "success")
        return redirect(url_for('index'))
        
    return render_template('signup.html', title=title, form=form)


@app.route('/address', methods=["GET", "POST"])
def address():
    title = 'Address'
    form = AddressForm()
    if form.validate_on_submit():
        name = form.name.data
        address = form.address.data
        phonenumber = form.phonenumber.data
        Address(name=name, address=address, phonenumber=phonenumber)
        return redirect(url_for('index'))
    return render_template('address.html', title=title, form=form)
