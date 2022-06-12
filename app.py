from flask import Flask, jsonify, request, render_template, session, redirect, url_for, send_file
from flask_cors import CORS
from load import load_portfolio

app = Flask(__name__, template_folder='site')
CORS(app)

@app.route('/')
def home():
    portData = load_portfolio('static/portfolio/list.csv')
    return render_template('index.html', portData=portData)

if __name__ == '__main__':
    app.run(debug=True)