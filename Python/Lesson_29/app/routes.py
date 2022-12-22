from turtle import title
from app import app, db, Tovar
from flask import redirect, render_template, url_for, request


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        title = request.form["title"]
        cost = request.form["cost"]
        info = request.form["info"]

        tovar = Tovar(title=title, cost=cost, info=info)
        try:
            db.session.add(tovar)
            db.session.commit()
            return redirect("/")
        except:
            return "Something went wrong..."
    else:
        return render_template("index.html")
