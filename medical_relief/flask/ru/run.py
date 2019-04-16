from flaskblog import app
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



if __name__ == "__main__":
    app.run(debug=True)
