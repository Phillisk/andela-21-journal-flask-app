from app import db, app
from werkzeug import generate_password_hash, check_password_hash



# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__ = True

    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


# Define a User model
class User(Base):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(128), nullable=False)
    lastname = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)
    
    # New instance instantiation procedure
    def __init__(self, firstname, lastname, username, email, password):

        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return '<User %r>' % self.username

    # generates a hash for storing password
    def set_password(self, password_string):
        self.password = generate_password_hash(password_string)

    # checks if password is in db
    def check_password(self, password_string):
        return check_password_hash(self.password, password_string)


class Journal(Base):
    """this is the  model for journals """
    __tablename__ = 'journal'
    
    # journal details
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.String(1000), nullable=False)
    tags = db.Column(db.String(50),  db.ForeignKey('tags.tagname'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

    def __init__(self, title, body, tags, user_id):
        self.title = title
        self.body = body
        self.tags = tags
        self.user_id = user_id

    def __repr__(self):
        return '<Journal %r>' % self.title




