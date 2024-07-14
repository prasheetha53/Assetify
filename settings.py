# settings.py

from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from flask_mongoengine import MongoEngine
from werkzeug.security import generate_password_hash
from ..models import User
from ..forms import SettingsForm

settings = Blueprint('settings', __name__, url_prefix='/api')

@settings.route("/settings", methods=['GET', 'POST'])
@login_required
def settings():
    form = SettingsForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.password = generate_password_hash(form.password.data, method='sha256')
        current_user.settings_completed = True
        current_user.save()
        flash('Settings updated successfully!', 'success')
        return redirect(url_for('dashboard'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('settings.html', form=form)
