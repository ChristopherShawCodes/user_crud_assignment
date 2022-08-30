from flask import render_template,request, redirect,session

from flask_app import app
from flask_app.models.user import User

#home route from landing page via index.html
@app.route("/")
def home():
    users = User.get_all()
    return render_template("index.html" ,users = users)

#routes to display all users from read(all)/html
@app.route('/users')
def display_all():
    users = User.get_all()
    return render_template("users.html", users = users)

@app.route('/user/new')
def new_user():
    users = User.get_all()
    return render_template("new_user.html", users = users)


@app.route('/user/create', methods=["POST"])
def create_user():
    data = {
    "first_name": request.form["first_name"],
    "last_name" : request.form["last_name"],
    "email" : request.form["email"]
    }
    print(request.form)
    print(data)
    User.save(data)
    new_user = User.get_last()
    id = new_user.id
    return redirect(f"/user/show/{id}")


@app.route('/user/show/<int:id>')
def show(id):
    data ={
        "id":id
    }
    print(data)
    user = User.get_one(data)
    print(user)
    print(user.first_name)
    return render_template("show_user.html", user=user)



@app.route('/user/edit/<int:id>')
def edit_user(id):
    data = {
        "id":id
    }
    user=User.get_one(data)
    return render_template('edit.html', user = user)



@app.route('/user/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
}
    User.destroy(data)
    return redirect('/users')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/create')