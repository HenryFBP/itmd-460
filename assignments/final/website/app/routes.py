from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/setup')
def setup():
    return render_template('setup.html')


@app.route('/your_first_app')
def your_first_app():
    return render_template('your_first_app.html')


@app.route('/coding_primer')
def coding_primer():
    return render_template('coding_primer.html')
