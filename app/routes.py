from app import app, forms
from flask import redirect, render_template, url_for, flash
from flask_login import login_required, login_user,logout_user, current_user, user_logged_in
from app.forms import SignUpForm, AddressForm, Loginform, PostForm
from app.models import User, Address, Post


@app.route('/')
def index():
	title = 'Home'
	posts = Post.query.all()
	return render_template('index.html', title=title, posts=posts)


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
        user = Address.query.filter_by(name=name).first()
        new_address = Address(name=name, address=address, phonenumber=phonenumber)
        flash(f'{user} has successfully added address', 'success')
        return redirect(url_for('index'))
        
    return render_template('address.html', title=title, form=form)

@app.route('/login', methods=["GET","POST"])
def login():
    title = 'Log In'
    form = Loginform()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash(f'{user} has successfully logged in', 'success')
            return redirect(url_for('index'))
        else:
            flash('Username and/or password is incorrect', 'danger')
        
    return render_template('login.html', title=title, form=form) 

@app.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out', 'primary')
    return redirect(url_for('index'))


@app.route('/create_post', methods=["GET","POST"] )
@login_required
def create_post():
    title = 'Create A Post'
    form = PostForm()
    if form.validate_on_submit():
        title =  form.title.data
        body = form.body.data
        new_post = Post(title=title, body=body)
        flash(f"{new_post.title} has been created", 'success')
        return redirect(url_for('index'))

    return render_template('create_post.html', title=title, form=form)
   
