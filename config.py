import os

basedir = os.path.abspath(os.path.dirname(__file__))
# para tratar o diretorio do projeto


class Config:
    db_path = os.path.join(basedir, "database.db")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
