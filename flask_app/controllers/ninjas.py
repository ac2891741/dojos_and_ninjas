from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html', dojos=Dojo.get_all())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/')

@app.route('/destroy/<int:ninja_id>/<int:dojo_id>')
def destroy(ninja_id, dojo_id):
    data = {
        'ninja_id': ninja_id,
    }
    Ninja.destroy(data)
    return redirect(f"/dojo/{dojo_id}")


@app.route('/edit/<int:id>')
def edit(id):
    data = {"id": id}
    
    return render_template('edit_ninja.html', ninja = Ninja.get_one(data))

