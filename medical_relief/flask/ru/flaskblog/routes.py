from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db, bcrypt
from flaskblog.forms import (LoginForm, RegistrationForm, UpdateAccountForm,
                             PostForm, UpdatePostForm,
                             RequestResetForm, ResetPasswordForm)
from flaskblog.models import User,News
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image


# About - first navbar section

@app.route("/")
@app.route("/home")
def home():
    # posts = News.query.order_by(News.id.desc()).limit(4).all()
    page = request.args.get('page', 1, type=int)
    posts = News.query.order_by(News.pub_date.desc()).paginate(page=page, per_page=4)
    # image_file = url_for('static', filename='post_pics/default.jpg')
    return render_template('01_home.html', posts=posts)


@app.route("/about_us")
def about_us():
    return render_template('11_about_us.html')


@app.route("/history")
def history():
    return render_template('12_history.html')


@app.route("/team")
def team():
    return render_template('13_team.html')


@app.route("/member_plus")
def member_plus():
    return render_template('14_member_plus.html')


@app.route("/more_about")
def more_about():
    return render_template('15_more_about.html')


# Programms - second navbar section

@app.route("/direct_one")
def direct_one():
    return render_template('21_program1.html')


@app.route("/direct_two")
def direct_two():
    return render_template('22_program2.html')


@app.route("/direct_three")
def direct_three():
    return render_template('23_program3.html')


@app.route("/direct_four")
def direct_four():
    return render_template('24_program4.html')


@app.route("/directs_all")
def directs_all():
    return render_template('25_programs.html')


# Treatment - third navbar section

@app.route("/treatment_one")
def treatment_one():
    return render_template('31_treat1.html')


@app.route("/treatment_two")
def treatment_two():
    return render_template('32_treat2.html')


@app.route("/treatment_three")
def treatment_three():
    return render_template('33_treat3.html')


@app.route("/treatment_four")
def treatment_four():
    return render_template('34_treat4.html')


@app.route("/treatments_all")
def treatments_all():
    return render_template('35_treats_all.html')


# Partners - fourth navbar section

@app.route("/hospitals")
def hospitals():
    return render_template('41_partner1.html')


@app.route("/doctors")
def doctors():
    return render_template('42_partner2.html')


@app.route("/partners_all")
def partners_all():
    return render_template('45_partners_all.html')


# News - fifth navbar section

@app.route("/news")
def news():
    page = request.args.get('page', 1, type=int)
    posts = News.query.order_by(News.pub_date.desc()).paginate(page=page, per_page=7)
    return render_template('51_news.html', posts=posts)


# Contacts - sixth navbar section

@app.route("/contacts")
def contacts():
    return render_template('61_contacts.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your acc created! You can login", 'success')
        return redirect(url_for('login'))
    return render_template('00_register.html', title = "Login-admin", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # flash(f"Welcome, {form.username.data}!", 'success')
        # return redirect(url_for('home'))
        user = User.query.filter_by(email=form.email.data).first()
        # password = User.query.filter_by(password=form.password.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login Unsuccessful. Please, go home and die!", 'danger')
    return render_template('00_login.html', title = "Login-admin", form=form)
    # return render_template('00_admin.html', posts = posts)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.split(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125,)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your acc has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/'+current_user.image_file)
    return render_template('00_account.html', title="Account", image_file=image_file, form=form)




def save_post_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.split(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/post_pics', picture_fn)
    output_size = (225, 225,)
    # i = Image.open(form_picture)
    # i.thumbnail(output_size)
    form_picture.save(picture_path)

    return picture_fn


@app.route("/posts/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        # if form.picture.data:
        # picture_file = save_post_picture(form.picture.data)
        # image_file = picture_file
        # else:
        #     # image_file = url_for('static', filename='post_pics/'+picture_file)
        # if form.picture.data != False:
        #     picture_file = save_post_picture(form.picture.data)
        #     picture = picture_file
        # picture = 'default.jpg'
        picture = form.file_name.data
        image_file = url_for('static', filename='post_pics/' + picture)

        post = News(title=form.title.data, content=form.content.data, image_file=image_file, )
        db.session.add(post)
        db.session.commit()
        flash('Post created', 'success')
        return redirect(url_for('home'))
    return render_template('00_create_post.html', title="New Post", form=form)


@app.route("/posts/<int:post_id>")
def post(post_id):
    post = News.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post,  image_file=post.image_file)

# @app.route("/posts/<int:post_id>/update", methods=['GET', 'POST'])
# @login_required
# def update_post(post_id):
#     post = News.query.get_or_404(post_id)
#     # if post.author != current_user
#     # if current_user:
#     #     abort(403)
#     form = PostForm()
#     if form.validate_on_submit():
#         post.title = form.title.data
#         post.content = form.content.data
#         db.session.commit()
#         flash('Post has beend updated', 'success')
#         return redirect(url_for('post', post_id=post.id))
#     elif request.method == "GET":
#         form.title.data = post.title
#         form.content.data = post.content
#     # return render_template('00_create_post.html', title="Update Post",
#     #                        form=form, legend="Update Post")
#     return render_template('00_create_post.html', title="Update Post",
#                            form=form)


@app.route("/posts/<int:post_id>/update", methods=['GET', 'POST'])
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
        return redirect(url_for('post', post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
        form.picture.data = post.image_file
    # return render_template('00_create_post.html', title="Update Post",
    #                        form=form, legend="Update Post")
    return render_template('00_create_post.html', title="Update Post",
                           form=form)


@app.route("/posts/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = News.query.get_or_404(post_id)

    # if post.author != current_user
    # if current_user:
    #     abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/user/<string:username>")
def user_post(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = News.query.filter_by(author=user).order_by(News.pub_date.desc()).paginate(page=page, per_page=4)
    return render_template('user_posts.html', posts=posts, user=user)

def send_reset_email(user):
    pass

@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instraction', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password',form=form)

@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash("That is an invalid token", 'warning')
        return redirect(url_for('reset_request'))
    form = RequestResetForm()
    return render_template('reset_token.html', title='Reset Password',form=form)


