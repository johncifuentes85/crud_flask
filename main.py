from flask import Flask, render_template, request, url_for, redirect
import controller

app = Flask(__name__)

"""
Definición de rutas
"""

@app.route("/")
@app.route("/index")
def index():
    users = controller.get_user()
    return render_template('index.html',users=users)

@app.route("/form_add_user")
def form_add_user():
    return render_template("add_user.html")

@app.route("/edit_user/<int:id>")
def edit_user(id):
    user = controller.get_user_id(id)
    return render_template("edit_user.html",user=user)

@app.route("update_user", methods=["POST"])
def update_user(id):
    #obtiende los datos que invoco el empoint
    id = request.form["id"]
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    passwd = request.form["passwd"]
    controller.update_user(id,name,email,phone,passwd)
    return redirect("/")

if __name__=="__main__":
    app.run(port=4500, debug=True)