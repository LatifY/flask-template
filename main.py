from flask import Flask, url_for, render_template, request, redirect, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "key"

@app.route("/")
def home():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return (render_template('404.html'), 404)