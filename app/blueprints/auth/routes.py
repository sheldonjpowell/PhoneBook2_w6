from flask import redirect, render_template, url_for, flash
from flask_login import login_required, login_user,logout_user, current_user, user_logged_in
from . import auth
from .forms import SignUpForm,Loginform
from .models import User


@auth.route('/signup', methods=["GET", "POST"])
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

        new_user = User(username=username, email=eblog.mail, password=password)

        flash(f"{new_user.username} has succesfully signed up.", "success")
        return redirect(url_for('blog.index'))
        
    return render_template('signup.html', title=title, form=form)


@auth.route('/login', methods=["GET","POST"])
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
            return redirect(url_for('blog.index'))
        else:
            flash('Username and/or password is incorrect', 'danger')
        
    return render_template('login.html', title=title, form=form)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out', 'primary')
    return redirect(url_for('blog.index'))


    