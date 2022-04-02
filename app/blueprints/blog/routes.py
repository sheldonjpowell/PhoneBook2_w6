from . import blog
from flask import redirect, render_template, url_for, flash
from flask_login import login_required, current_user
from .forms import AddressForm, PostForm
from .models import Address, Post


@blog.route('/')
def index():
	title = 'Home'
	posts = Post.query.all()
	return render_template('index.html', title=title, posts=posts)



@blog.route('/address', methods=["GET", "POST"])
def address():
    title = 'Address'
    form = AddressForm()
    if form.validate_on_submit():
        name = form.name.data
        address = form.address.data
        phonenumber = form.phonenumber.data
        # user = Address.query.filter_by(name=name).first()
        users_with_that_info = Address.query.filter((Address.name==name))
        if users_with_that_info:
            flash(f"There is already a name addressed to your number", "danger")
            return redirect(url_for('blog.address'))

        # new_address = Address(name=name, address=address, phonenumber=phonenumber, user_id=current_user.id)
        flash(f'{name} has successfully added address', 'success')
        return redirect(url_for('blog.index'))

    return render_template('address.html', title=title, form=form)


@blog.route('/create_post', methods=["GET","POST"] )
@login_required
def create_post():
    title = 'Create A Post'
    form = PostForm()
    if form.validate_on_submit():
        title =  form.title.data
        body = form.body.data
        new_post = Post(title=title, body=body, user_id=current_user.id)
        flash(f"{new_post.title} has been created", 'success')
        return redirect(url_for('blog.index'))

    return render_template('create_post.html', title=title, form=form)
   
@blog.route('/my_posts')
@login_required
def my_posts():
    title = 'My Posts'
    form = PostForm()
    posts = current_user.posts.all()
    return render_template('my_posts.html', title=title, posts=posts, form=form)

@blog.route('/my_address')
def my_address():
    title = 'My Address'
    form = AddressForm()
    address = current_user.address.all()
    return render_template('my_address.html', title=title, address=address, form=form)