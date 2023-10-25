"""Data models."""
import datetime
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from server import db


# The User class is a data model for user accounts
class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.Boolean)
    image = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=True)

    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")
        self.name = kwargs.get("name")
        self.age = kwargs.get("age")
        self.gender = kwargs.get("gender")
        self.image = kwargs.get("image")
        self.created = kwargs.get("created")

    def __repr__(self):
        """
        The __repr__ function is used to return a string representation of the object
        :return: The name of the user.
        """
        return "<User {}>".format(self.name)

    def hash_password(self):
        """
        It takes the password that the user has entered, hashes it, and then stores the hashed password in
        the database
        """
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        """
        It takes a plaintext password, hashes it, and compares it to the hashed password in the database

        :param password: The password to be hashed
        :return: The password is being returned.
        """
        return check_password_hash(self.password, password)
