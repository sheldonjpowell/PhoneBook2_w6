from crypt import methods
from turtle import title

from app.blueprints.auth.forms import SearchForm
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
@login_required
def address():
    title = 'Address'
    form = AddressForm()
    if form.validate_on_submit():
        name = form.name.data
        address = form.address.data
        phonenumber = form.phonenumber.data
        # user = Address.query.filter_by(name=name).first()
        # users_with_that_info = Address.query.filter((Address.name==name))
        new_address = Address(name=name, address=address, phonenumber=phonenumber, user_id=current_user.id)
        flash(f'{name} has successfully added address', 'success')
        return redirect(url_for('blog.index'))

    return render_template('address.html', title=title, form=form)



@blog.route('/my_address')
def my_address():
    title = 'My Address'
    form = AddressForm()
    address = current_user.address.all()
    return render_template('my_address.html', title=title, address=address, form=form)

@blog.route('/address/<address_id>')
@login_required
def single_address(address_id):
    address = Address.query.get_or_404(address_id)
    title = address.name
    return render_template('address_detail.html', title=title, address=address)

@blog.route('/edit_address/<address_id>', methods=["GET", "POST"])
@login_required
def edit_address(address_id):
    address = Address.query.get_or_404(address_id)
    if address.author != current_user:
        flash('You do not have edit access to this post.', 'danger')
        return redirect(url_for('blog.my_address'))
    title = f"Edit {address.name}"
    form = AddressForm()
    if form.validate_on_submit():
        address.update(**form.data)
        flash(f'{address.name} has been updated', 'warning')
        return redirect(url_for('blog.my_address'))
    return render_template('address_edit.html', title=title , address=address, form=form)


@blog.route('/delete_address/<address_id>')
@login_required
def delete_address(address_id):
    address = Address.query.get_or_404(address_id)
    if address.author != current_user:
        flash('You do not have delete access to the address', 'danger')
    else:
        address.delete()
        flash(f'{address.name} has been deleted.', 'secondary')
    print(current_user)
    return redirect(url_for('blog.my_address'))
 





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




@blog.route('/search_posts', methods=['GET', 'POST'])
def search_posts():
    title = 'Search'
    form =  SearchForm()
    posts = []
    if form.validate_on_submit():
        term = form.search.data
        posts = Post.query.filter( (Post.title.ilike(f'%{term}%')) | (Post.body.ilike(f'%{term}%')) ).all()

    return render_template('search_posts.html', title=title, posts=posts, form=form)



@blog.route('/posts/<post_id>')
@login_required
def single_post(post_id):
    post = Post.query.get_or_404(post_id)
    title = post.title
    return render_template('post_detail.html', title=title, post=post)



@blog.route('/edit_posts/<post_id>', methods=["GET", "POST"] )
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flash('You do not have edit access to this post.', 'danger')
        return redirect(url_for('blog.my_posts'))
    title= f"Edit {post.title}"
    form = PostForm()
    if form.validate_on_submit():
        post.update(**form.data)
        flash(f'{post.title} has been updated', 'warning')
        return redirect(url_for('blog.my_posts'))
    return render_template('post_edit.html', title=title, post=post, form=form)



@blog.route('/delete_posts/<post_id>')
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flash('You do not have delete access to this post', 'danger')
    else:
        post.delete()
        flash(f'{post.title} has been deleted.', 'secondary')
    return redirect(url_for('blog.my_posts'))


# @blog.route('/address/<address_id>')

# def single_addresss(address_id):
#     address = Address.query.get_or_404(address_id)
#     return str(address)

