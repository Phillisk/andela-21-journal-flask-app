# Import flask and template operators
from flask import Flask, render_template

# Import extensions e.g. SQLAlchemy, flask-restful
#from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
#from flask_restful import Api

# Define the WSGI application object and api
app = Flask(__name__)

#api = Api(mod_main)


# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers and flask_migrate for migrations
db = SQLAlchemy(app)

#settings for flask login
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'auth.login'

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)

from app.main.views import mod_main as main_module
from app.auth.views import mod_auth as auth_module


# Register blueprint(s)
app.register_blueprint(main_module)
app.register_blueprint(auth_module)
#api.add_resource()
# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()



