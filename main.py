from flask import Flask, url_for, render_template, request, redirect, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "key"

@app.route("/")
def home():
    return render_template('index.html')