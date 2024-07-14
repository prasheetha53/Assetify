# login.py

from flask import Blueprint, jsonify, request, flash, redirect, url_for
from flask_login import login_user
from werkzeug.security import check_password_hash
from ..models import User
from ..forms import LoginForm

login = Blueprint('login', __name__, url_prefix='/api')

@login.route("/login", methods=['POST'])
def login_user():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing JSON data'}), 400

    form = LoginForm(data=data)
    if form.validate():
        user = User.objects(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid email or password'}), 401
    else:
        return jsonify({'error': form.errors}), 400
