from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import current_user, login_required
from website import db
from website.models import BlogPost
from website.blogs.forms import BlogPostForm

blogs = Blueprint('blogs', __name__)

# Create
@blogs.route('/create', methods=['POST', 'GET'])
@login_required
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():
        blog_post = BlogPost(title=form.title.data, 
            text=form.text.data, user_id=current_user.id)
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog created!')
        return redirect(url_for('core.index'))
    
    return render_template('create_post.html', form=form)

# View blog
@blogs.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html', title=blog_post.title, 
        date=blog_post.date, post=blog_post)


# Update 
@blogs.route('/<int:blog_post_id>/update', methods=['GET', 'POST'])
@login_required
def update(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    if blog_post.author != current_user:
        abort(403)
        print('Not authorized user')

    form = BlogPostForm()
    if form.validate_on_submit():
        blog_post.title = form.title.data
        blog_post.text = form.text.data
        db.session.commit()
        flash('Blog updated!')
        return redirect(url_for('blogs.blog_post', blog_post_id=blog_post.id))
    elif request.method == 'GET':
        # Fill up the original data
        form.title.data = blog_post.title
        form.text.data = blog_post.text
    
    return render_template('create_post.html', form=form)

# Delete
@blogs.route('/<int:blog_post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)
        print('Delete post: Not authorized user')
    
    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog post delete!')
    return redirect(url_for('core.index'))
