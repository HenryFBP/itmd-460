from flask import render_template

from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/intro')
def intro():
    return render_template('intro.html')
