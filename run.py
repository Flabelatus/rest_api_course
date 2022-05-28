from app import app
from db import db

db.init_app(app)


# In order to have the SQLAlchemy creating the database and tables
@app.before_first_request
def create_tables():
    db.create_all()
