from flask import Flask, render_template, url_for

app = Flask(__name__)

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

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)


@app.route("/about_us")
def about_us():
    return render_template('about_us.html', posts = posts)


@app.route("/history")
def history():
    return render_template('history.html', posts = posts)

@app.route("/team")
def team():
    return render_template('team.html', posts = posts)

@app.route("/member_plus")
def member_plus():
    return render_template('member_plus.html', posts = posts)

@app.route("/more_about")
def more_about():
    return render_template('more_about.html', posts = posts)


if __name__ == "__main__":
    app.run(debug=True)


