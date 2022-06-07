from sqlalchemy import false
from models import db, Process

from flask import Flask, abort, redirect, render_template, request, url_for
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'



## INSERT -> Nr Jobs e Nr Tasks ##

@app.route('/create' , methods = ['GET','POST'])

def create():
 
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':

        values = request.form.to_dict(flat = false)
        id = values['id'][0]
        task_id = values['task_id'][0]
        process = Process(id = id, task_id = task_id)
        db.session.add(process)
        db.session.commit()
        return redirect('/data')


@app.route('/data')

def showAll():
    processes = Process.query.all()
    return render_template('showAll.html',processes = processes)


@app.route('/data/<int:id>')

def showSingle(id):
    process = Process.query.filter_by(id = id).first()
    if process:
        return render_template('info.html', process = process)

    return f"Process {id} doesn't exist!"


@app.route('/data/<int:id>/delete', methods=['GET','POST'])

def delete(id):
    process = Process.query.filter_by(id=id).first()
    if request.method == 'POST':
        if process:
            db.session.delete(process)
            db.session.commit()
            return render_template('404.html')
        abort(404)
        
 
    return render_template('delete.html')

@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method=='GET':
        return render_template('create.html')

    elif request.method=='POST':
        return "OK this is a post method"
    else:
        return("ok")


app.run(host='localhost', port=5000)
