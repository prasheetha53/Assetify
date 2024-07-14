# routes/register.py
from flask import Blueprint, jsonify, request
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_login import login_user
from werkzeug.security import generate_password_hash
from forms import RegistrationForm  # Adjust the import path as needed
from models import User  # Adjust the import path as needed

register = Blueprint('register', __name__, url_prefix='/register')

@register.route("/", methods=['POST'])
def register_user():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing JSON data'}), 400

    form = RegistrationForm(data=data)
    if form.validate():
        existing_user = User.objects(email=form.email.data).first()
        if existing_user:
            return jsonify({'error': 'Email already exists'}), 409

        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        new_user.save()
        return jsonify({'message': 'Registration successful'}), 201
    else:
        return jsonify({'error': form.errors}), 400
