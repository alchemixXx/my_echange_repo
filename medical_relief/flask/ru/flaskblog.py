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


@app.route("/about")
def about():
    return render_template('about.html', posts = posts)


@app.route("/history")
def history():
    return render_template('history.html', posts = posts)


if __name__ == "__main__":
    app.run(debug=True)





first = "120"
print(type(first))