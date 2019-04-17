from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import LoginForm, RegistrationForm
from flaskblog.models import User,News
from flask_login import login_user, current_user


posts = [
    {
        'url':'http://127.0.0.1:5000',
        # 'author': "Corney Schafter",
        # 'title': "Blog post 1",
        # 'content': 'First blog post',
        # 'date': 'April 20, 2018',
    },
    {
        # 'author': "Pavel D",
        # 'title': "Blog post 2",
        # 'content': 'Second blog post',
        # 'date': 'April 21, 2018',
    },
]


# About - first navbar section

@app.route("/")
@app.route("/home")
def home():
    return render_template('01_home.html', posts = posts)


@app.route("/about_us")
def about_us():
    return render_template('11_about_us.html', posts = posts)


@app.route("/history")
def history():
    return render_template('12_history.html', posts = posts)


@app.route("/team")
def team():
    return render_template('13_team.html', posts = posts)


@app.route("/member_plus")
def member_plus():
    return render_template('14_member_plus.html', posts = posts)


@app.route("/more_about")
def more_about():
    return render_template('15_more_about.html', posts = posts)


# Programms - second navbar section

@app.route("/direct_one")
def direct_one():
    return render_template('21_program1.html', posts = posts)


@app.route("/direct_two")
def direct_two():
    return render_template('22_program2.html', posts = posts)


@app.route("/direct_three")
def direct_three():
    return render_template('23_program3.html', posts = posts)


@app.route("/direct_four")
def direct_four():
    return render_template('24_program4.html', posts = posts)


@app.route("/directs_all")
def directs_all():
    return render_template('25_programs.html', posts = posts)


# Treatment - third navbar section

@app.route("/treatment_one")
def treatment_one():
    return render_template('31_treat1.html', posts = posts)


@app.route("/treatment_two")
def treatment_two():
    return render_template('32_treat2.html', posts = posts)


@app.route("/treatment_three")
def treatment_three():
    return render_template('33_treat3.html', posts = posts)


@app.route("/treatment_four")
def treatment_four():
    return render_template('34_treat4.html', posts = posts)


@app.route("/treatments_all")
def treatments_all():
    return render_template('35_treats_all.html', posts = posts)


# Partners - fourth navbar section

@app.route("/hospitals")
def hospitals():
    return render_template('41_partner1.html', posts = posts)


@app.route("/doctors")
def doctors():
    return render_template('42_partner2.html', posts = posts)


@app.route("/partners_all")
def partners_all():
    return render_template('45_partners_all.html', posts = posts)


# News - fifth navbar section

@app.route("/news")
def news():
    return render_template('51_news.html', posts = posts)


# Contacts - sixth navbar section

@app.route("/contacts")
def contacts():
    return render_template('61_contacts.html', posts = posts)


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
    return render_template('00_login.html', title = "Login-admin", form=form, posts = posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # flash(f"Welcome, {form.username.data}!", 'success')
        # return redirect(url_for('home'))
        user = User.query.filter_by(email=form.email.data)
        password = User.query.filter_by(password=form.password.data).first()
        if user and password:
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful. Please, go home and die!", 'danger')
    return render_template('00_login.html', title = "Login-admin", form=form, posts = posts)
    # return render_template('00_admin.html', posts = posts)

