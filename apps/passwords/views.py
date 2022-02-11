from flask import Blueprint, request, url_for, redirect, render_template

passwords = Blueprint('passwords', __name__, template_folder='templates/passwords')


@passwords.route('/passwords-list')
def all_pass():
    return render_template('passwords-list.html')
