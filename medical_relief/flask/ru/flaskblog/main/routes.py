from flask import render_template, request, Blueprint

from flaskblog.models import User, News

main = Blueprint('main', __name__)


# About - first navbar section

@main.route("/")
@main.route("/home")
def home():
    # posts = News.query.order_by(News.id.desc()).limit(4).all()
    page = request.args.get('page', 1, type=int)
    posts = News.query.order_by(News.pub_date.desc()).paginate(page=page, per_page=4)
    # image_file = url_for('static', filename='post_pics/default.jpg')
    return render_template('01_home.html', posts=posts)


@main.route("/about_us")
def about_us():
    return render_template('11_about_us.html')


@main.route("/history")
def history():
    return render_template('12_history.html')


@main.route("/team")
def team():
    return render_template('13_team.html')


@main.route("/member_plus")
def member_plus():
    return render_template('14_member_plus.html')


@main.route("/more_about")
def more_about():
    return render_template('15_more_about.html')


# Programms - second navbar section

@main.route("/direct_one")
def direct_one():
    return render_template('21_program1.html')


@main.route("/direct_two")
def direct_two():
    return render_template('22_program2.html')


@main.route("/direct_three")
def direct_three():
    return render_template('23_program3.html')


@main.route("/direct_four")
def direct_four():
    return render_template('24_program4.html')


@main.route("/directs_all")
def directs_all():
    return render_template('25_programs.html')


# Treatment - third navbar section

@main.route("/treatment_one")
def treatment_one():
    return render_template('31_treat1.html')


@main.route("/treatment_two")
def treatment_two():
    return render_template('32_treat2.html')


@main.route("/treatment_three")
def treatment_three():
    return render_template('33_treat3.html')


@main.route("/treatment_four")
def treatment_four():
    return render_template('34_treat4.html')


@main.route("/treatments_all")
def treatments_all():
    return render_template('35_treats_all.html')


# Partners - fourth navbar section

@main.route("/hospitals")
def hospitals():
    return render_template('41_partner1.html')


@main.route("/doctors")
def doctors():
    return render_template('42_partner2.html')


@main.route("/partners_all")
def partners_all():
    return render_template('45_partners_all.html')


# News - fifth navbar section

@main.route("/news")
def news():
    page = request.args.get('page', 1, type=int)
    posts = News.query.order_by(News.pub_date.desc()).paginate(page=page, per_page=7)
    return render_template('51_news.html', posts=posts)


# Contacts - sixth navbar section

@main.route("/contacts")
def contacts():
    return render_template('61_contacts.html')

@main.route("/support_pr")
def help_us():
    return render_template('71_help_us.html')