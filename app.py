from flask import Flask, jsonify, request, render_template, session, redirect, url_for, send_file
from flask_cors import CORS

app = Flask(__name__, template_folder='site')
CORS(app)

@app.route('/')
def home():
    return(render_template('index.html'))

if __name__ == '__main__':
    app.run(debug=True)