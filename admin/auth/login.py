from typing import Any, Union

from flask import Blueprint, render_template, url_for, redirect, flash, request, Response
from flask_login import login_user, logout_user

from models.user import User


admin_login = Blueprint('admin_login', __name__)

@admin_login.route('/admin/user/login', methods=['GET', 'POST'])
def login() -> Union[Response, Any]:
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email and password:
            user = User.authenticate(email, password)
            if not user:
                flash("Veuillez compléter correctement les champs « email » et « mot de passe » d'un compte administracteur.")
                return render_template('admin/login.html')
            if not user.isActive or not user.isStaff or not user.isAdmin:
                flash("Veuillez compléter correctement les champs « email » et « mot de passe » d'un compte administracteur.")
                return render_template('admin/login.html')
            login_user(user)
            return redirect(url_for('admin.index'))
    return render_template('admin/login.html')

@admin_login.route('/admin/user/logout')
def logout()-> Response:
    logout_user()
    return redirect(url_for('home'))
