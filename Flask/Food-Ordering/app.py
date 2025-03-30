from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///menu.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/menu')
def menu():
    items = MenuItem.query.all()
    return render_template("menu.html", items = items)


@app.route('/menu/add', methods=["POST"])
def add_item():
    name = request.form["name"]
    quantity = request.form["quantity"]

    new_item = MenuItem(name = name, quantity = int(quantity))
    db.session.add(new_item)
    db.session.commit()
    
    return redirect(url_for("menu"))


@app.route('/menu/edit/<int:item_id>')
def edit_item(item_id):
    item = MenuItem.query.get(item_id)
    return render_template("edit.html", item = item)

@app.route("/menu/update/<int:item_id>", methods=["POST"])
def update_item(item_id):
    item = MenuItem.query.get(item_id)
    item.name = request.form["name"]
    item.quantity = int(request.form["quantity"])

    db.session.commit()
    return redirect(url_for("menu"))

@app.route("/menu/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    item = MenuItem.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("menu"))

if __name__ == "__main__":
    app.run(debug=True)
