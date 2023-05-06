import os
import requests
from uuid import uuid4
from flask import Flask, render_template, request, Response, redirect, flash

app = Flask(name)
app.config['SECRET_KEY'] = str(uuid4())


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if 'url' not in request.form:
        return render_template('index.html', error='Invalid form submission')

    url = request.form['url']
    response = requests.get(url);
    return render_template('index.html')


if name == 'main':
    app.run(host="0.0.0.0", port=5000)