from flask import Flask, render_template, url_for

app = Flask(__name__)

# this is second test comment

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
def progr_one():
    return render_template('21_program1.html', posts = posts)


@app.route("/direct_two")
def progr_two():
    return render_template('22_program2.html', posts = posts)


@app.route("/direct_three")
def progr_three():
    return render_template('23_program3.html', posts = posts)


@app.route("/direct_four")
def progr_frou():
    return render_template('24_program4.html', posts = posts)


@app.route("/directs_all")
def progrs_all():
    return render_template('25_programs.html', posts = posts)


# Treatment - third navbar section

@app.route("/treatment_one")
def treat_one():
    return render_template('31_treat1.html', posts = posts)


@app.route("/treatment_two")
def treat_two():
    return render_template('32_treat2.html', posts = posts)


@app.route("/treatment_three")
def treat_three():
    return render_template('33_treat3.html', posts = posts)


@app.route("/treatment_four")
def treat_four():
    return render_template('34_treat4.html', posts = posts)


@app.route("/treatments_all")
def treats_all():
    return render_template('35_treats_all.html', posts = posts)


# Partners - fourth navbar section

@app.route("/hospitals")
def hospitals():
    return render_template('41_partner1.html', posts = posts)


@app.route("/doctors")
def doctors():
    return render_template('42_partner2.html', posts = posts)


@app.route("/partners_all")
def partns_all():
    return render_template('45_partners_all.html', posts = posts)


# News - fifth navbar section

@app.route("/news")
def news():
    return render_template('51_news.html', posts = posts)


# Contacts - sixth navbar section

@app.route("/contacts")
def contacts():
    return render_template('61_contacts.html', posts = posts)



if __name__ == "__main__":
    app.run(debug=True)
