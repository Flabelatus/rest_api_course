from db import db


class ItemModel(db.Model):
    """
    The Item model class to include the main attributes and methods representing
    the items in the Store application.

        Attributes:
             name [str]: The name of the item
             price [float]: The price for each item
             store_id [int]: The id of the store that the item belongs to. Mainly
                for the database table reference

        Methods:
            json:
                Create JSON object from the item
                :return A dictionary containing the item name and the item price
                    representing the item as JSON.

            find_by_name:
                Find the item by the `name` from the database.
                :param `name` of the item to find from database
                :return The item that was searched from the database

            save_to_db
                Add the item to the database and commits

            delete_from_db
                Deletes the item from the database and commits

    The following is a set of code lines to add in order to set up the connection
    between the SQLAlchemy and the Flask app. It is important to have the models
    connected to the SQLAlchemy database in order to create the related tables.
    """
    __tablename__ = 'items'

    # Adding the id, name and price in the rows in the db
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    # For relational purpose to connect the table with the different table (Using Foreign Key).
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
