from app import app
from flask import redirect, url_for
# from flask_login import login_required, current_user
# from app.forms import AddressForm, PostForm
# from app.models import Address, Post


@app.route('/')
def index():
    return redirect(url_for('blog.index'))




# @app.route('/address', methods=["GET", "POST"])
# def address():
#     title = 'Address'
#     form = AddressForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         address = form.address.data
#         phonenumber = form.phonenumber.data
#         # user = Address.query.filter_by(name=name).first()
#         new_address = Address(name=name, address=address, phonenumber=phonenumber)
#         flash(f'{name} has successfully added address', 'success')
#         return redirect(url_for('index'))
        
#     return render_template('address.html', title=title, form=form)


# @app.route('/create_post', methods=["GET","POST"] )
# @login_required
# def create_post():
#     title = 'Create A Post'
#     form = PostForm()
#     if form.validate_on_submit():
#         title =  form.title.data
#         body = form.body.data
#         new_post = Post(title=title, body=body, user_id=current_user.id)
#         flash(f"{new_post.title} has been created", 'success')
#         return redirect(url_for('index'))

#     return render_template('create_post.html', title=title, form=form)
   
# @app.route('/my_posts')
# @login_required
# def my_posts():
#     title = 'My Posts'
#     form = PostForm()
#     posts = current_user.posts.all()
#     return render_template('my_posts.html', title=title, posts=posts, form=form)