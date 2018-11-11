from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/audio')
def audio():
    return render_template('audio.html')


@app.route('/video')
def video():
    return render_template('video.html')


@app.route('/images')
def images():
    return render_template('images.html')
