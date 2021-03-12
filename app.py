from flask import Flask, jsonify, request, render_template, session, redirect, url_for
from flask_cors import CORS
from functionSBD import *

app = Flask(__name__, template_folder='site')
CORS(app)

@app.route('/')
def home():
    return(render_template('index.html'))

@app.route('/about')
def about():
    return(render_template('404.html'))

# ==============================================================
# Route of Projects
# ==============================================================

# Sentence Boundary Disambiguation
@app.route('/ports/sbd-project', methods=['GET','POST'])
def sbd():
    if request.method == 'GET':
        return(render_template('projects/sentence_boundary_disambiguation/sentence_boundary_disambiguation.html'))
    if request.method == 'POST':
        temp_query = request.form['query']
        temp_result = sent_segment_svc(temp_query)
        # temp_result = temp_query.lower()
        return render_template('projects/sentence_boundary_disambiguation/demo-result.html', original_input=temp_query, result=temp_result)

if __name__ == '__main__':
    app.run()