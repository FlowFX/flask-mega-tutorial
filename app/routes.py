from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Florian'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Hamburg!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Matrix movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
