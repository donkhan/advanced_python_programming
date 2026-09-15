from flask import Flask, request, render_template_string, redirect
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas connection
# client = MongoClient("<MongoDB Atlas connection string>")
client = MongoClient("mongodb://localhost:27017")
db = client["college"]
users = db["users"]


HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>User Management</title>
</head>
<body>

<h1>User Management System</h1>

<h2>Add User</h2>

<form method="POST" action="/add">
    Name:
    <input type="text" name="name" required>

    Age:
    <input type="number" name="age" required>

    Email:
    <input type="email" name="email" required>

    <input type="submit" value="Add User">
</form>

<hr>

<h2>Users</h2>

{% for user in users %}

<p>
    <b>Name:</b> {{ user["name"] }}
    <br>
    <b>Age:</b> {{ user["age"] }}
    <br>
    <b>Email:</b> {{ user["email"] }}

    <br><br>

    <a href="/update/{{ user['_id'] }}">Update</a>

    <a href="/delete/{{ user['_id'] }}">Delete</a>
</p>

<hr>

{% endfor %}

</body>
</html>
"""


# CREATE
@app.route("/add", methods=["POST"])
def add_user():

    user = {
        "name": request.form["name"],
        "age": int(request.form["age"]),
        "email": request.form["email"]
    }

    users.insert_one(user)

    return redirect("/")


# READ
@app.route("/")
def show_users():

    user_list = users.find()

    return render_template_string(
        HTML,
        users=user_list
    )


# UPDATE
@app.route("/update/<user_id>")
def update_user(user_id):

    from bson.objectid import ObjectId

    users.update_one(
        {"_id": ObjectId(user_id)},
        {
            "$set": {
                "email": "updated@example.com"
            }
        }
    )

    return redirect("/")


# DELETE
@app.route("/delete/<user_id>")
def delete_user(user_id):

    from bson.objectid import ObjectId

    users.delete_one(
        {"_id": ObjectId(user_id)}
    )

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)