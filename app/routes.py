from flask import request, redirect, url_for, render_template
from app import app, db
from app.models import Item


@app.route("/")
def index():
    # mostrar todos os itens do banco de dados
    items_ = Item.query.all()
    return render_template("index.html", items=items_)


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":  # inserir informações
        modelo = request.form["modelo"]
        marca = request.form["marca"]
        ano = request.form["ano"]
        description = request.form["description"]
        new_item = Item(modelo=modelo, marca=marca, ano=ano, description=description)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("create.html")  # so abre o formulario


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    item = Item.query.get_or_404(id)
    if request.method == "POST":
        item.modelo = request.form["modelo"]
        item.marca = request.form["marca"]
        item.ano = request.form["ano"]
        item.description = request.form["description"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("update.html", item=item)


@app.route("/delete/<int:id>")
def delete(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("index"))
