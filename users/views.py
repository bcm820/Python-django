from __future__ import unicode_literals
from django.shortcuts import render

# practice form validation
# create Django form version with its form validation?

def index():
    users = { "users": User.objects.all() }
    return render(request, 'users/index.html', users)

def new():
    users = { "users": User.objects.all() }
    return render(request, 'users/new.html', users)

def show(id):
    user = { "user": User.objects.get(id=id) }
    return render(request, 'users/show.html', user)

def edit(id):
    user = { "user": User.objects.get(id=id) }
    return render(request, 'users/edit.html', user)

def create():

    User.objects.create(
        name = request.POST['name'],
        email = request.POST['email']
    )
    
    id = User.objects.last().id
    return redirect('/users/' + id)
    

# UPDATE: Update record by ID
@app.route('/users/<user_id>/update/', methods=['POST'])
def update(user_id):
    
    query = "UPDATE users SET name = :name, email = :email WHERE id = :id"
    data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'id': user_id
        }
    mysql.query_db(query, data)
    return redirect('/users/{}/'.format(user_id))


# DESTROY: Delete record by ID
@app.route('/users/<user_id>/destroy/', methods=['POST'])
def destroy(user_id):
    query = "DELETE FROM users WHERE id = :id"
    data = {'id': user_id}
    mysql.query_db(query, data)
    return redirect('/users/')