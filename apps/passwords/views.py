from flask import Blueprint, request, url_for, redirect, render_template, flash
from apps.passwords.models import Password
from database.database import db


passwords = Blueprint('passwords', __name__, template_folder='templates/passwords')


@passwords.route('/passwords-list')
def all_pass():
    return render_template('passwords-list.html')

@passwords.route('/get-passwords/<string:passwordId>')
def get_password(passwordId):
    return f"get password {passwordId}"

@passwords.route('/new-passwords', methods=['POST'])
def new_password():
    website = request.form['website']
    email = request.form['email']
    password = request.form['password']
    new_password = Password(website, email, password)
    db.session.add(new_password)
    db.session.commit()
    return 'new password'

@passwords.route('/update-passwords/<string:passwordId>')
def update_password(passwordId):
    return f"update password {passwordId}"

@passwords.route('/delete-passwords/<string:passwordId>')
def delete_password(passwordId):
    return f"delete password {passwordId}"
