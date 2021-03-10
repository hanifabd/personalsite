from flask import Flask, jsonify, request, render_template, session, redirect, url_for
from flask_cors import CORS
from pickle import load
import re

app = Flask(__name__, template_folder='site')
CORS(app)

@app.route('/')
def home():
    return(render_template('index.html'))

@app.route('/about')
def about():
    return(render_template('404.html'))

if __name__ == '__main__':
    app.run()