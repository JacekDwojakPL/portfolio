from flask import Flask, render_template, jsonify, request, url_for
from flask_jsglue import JSGlue

app = Flask(__name__)
jsglue = JSGlue(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/portfolio/<product>')
def portfolio(product):
    page = product + '.html'
    return render_template(page)
