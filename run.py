from app import app, db

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # caso nao tenha uma tabela, ele vai criar
    app.run(debug=True)
