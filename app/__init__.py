# Import flask and template operators
from flask import Flask, render_template

# Import extensions e.g. SQLAlchemy, flask-restful
#from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Api

# Define the WSGI application object and api
app = Flask(__name__)

api = Api(mod_main)


# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers and flask_migrate for migrations
db = SQLAlchemy(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)

from app.main.api import main as main_module

# Register blueprint(s)
app.register_blueprint(mod_main)
#api.add_resource()
# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()



