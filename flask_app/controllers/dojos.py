from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojo_home():
    
    return render_template("index.html", dojos = Dojo.get_all())

@app.route('/dojos/create', methods=['POST'])
def create():
    Dojo.save(request.form)
    
    return redirect("/dojos")

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo.html', dojo=Dojo.get_one(data))

@app.route('/update', methods=['POST'])
def update():
    data ={
        "id" : request.form['id'],
        "dojo_id" : request.form['dojo_id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
    }

    Ninja.update(data)
    # dojo_id = request.form['dojo_id']
    return redirect(f"/dojo/{request.form['dojo_id']}")

