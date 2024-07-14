# app.py
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_mongoengine import MongoEngine
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm, SettingsForm  # Assuming forms.py is in the main directory

import secrets

# Generate a secure secret key
secret_key = secrets.token_hex(32)

# Flask configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.config['MONGODB_SETTINGS'] = {
    'db': 'assetify_db',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model
class User(UserMixin, db.Document):
    username = db.StringField(max_length=20, unique=True, required=True)
    email = db.EmailField(unique=True, required=True)
    password = db.StringField(required=True)
    settings_completed = db.BooleanField(default=False)

@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()

# No need to define routes here, they will be defined in each blueprint module

if __name__ == '__main__':
    app.run(debug=True)
