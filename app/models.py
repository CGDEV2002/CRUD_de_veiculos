from app import db


# modelo do banco de dados
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=True)
