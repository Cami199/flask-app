from flask import Flask, render_template, request, redirect, url_for, Blueprint


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    
    return render_template('login/auth.html')