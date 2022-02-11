from flask import Blueprint, request, url_for, redirect, render_template, flash

users = Blueprint('users', __name__, template_folder='templates/users')

@users.route('/login')
def login():
    return render_template('login.html')

@users.route('/register')
def register():
    return render_template('register.html')
