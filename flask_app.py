
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hello_world():
    return 'project2'

@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/init')
def initTable():
    try:
        return 'init ok'
    except expression as ex:
        return ex

@app.route("/insert", methods=["POST"])
def insert():
    return 'ok'