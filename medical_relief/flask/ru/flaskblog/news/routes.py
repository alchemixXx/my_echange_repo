from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskblog import db, bcrypt, mail
from flaskblog.news.forms import PostForm, UpdatePostForm
from flaskblog.models import User, News
from flask_login import login_required


posts = Blueprint('posts', __name__)

# About - first navbar section

@posts.route("/posts/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        picture = form.file_name.data
        image_file = url_for('static', filename='post_pics/' + picture)
        post = News(title=form.title.data, content=form.content.data, image_file=image_file, )
        db.session.add(post)
        db.session.commit()
        flash('Post created', 'success')
        return redirect(url_for('main.home'))
    return render_template('00_create_post.html', title="New Post", form=form)


@posts.route("/posts/<int:post_id>")
def post(post_id):
    post = News.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post,  image_file=post.image_file)

@posts.route("/posts/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = News.query.get_or_404(post_id)
    # if post.author != current_user
    # if current_user:
    #     abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        picture = form.file_name.data
        image_file = url_for('static', filename='post_pics/' + picture)

        db.session.commit()
        flash('Post has beend updated', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
        form.picture.data = post.image_file
    # return render_template('00_create_post.html', title="Update Post",
    #                        form=form, legend="Update Post")
    return render_template('00_create_post.html', title="Update Post",
                           form=form)


@posts.route("/posts/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = News.query.get_or_404(post_id)

    # if post.author != current_user
    # if current_user:
    #     abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted!', 'success')
    return redirect(url_for('main.home'))
