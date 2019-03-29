from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': "Corney Schafter",
        'title': "Blog post 1",
        'content': 'First blog post',
        'date': 'April 20, 2018',
    },
    {
        'author': "Pavel D",
        'title': "Blog post 2",
        'content': 'Second blog post',
        'date': 'April 21, 2018',
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', post = posts)


@app.route("/about")
def about():
    return "About page!"


if __name__ == "__main__":
    app.run(debug=True)
