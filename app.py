from flask import Flask, render_template, request, redirect, url_for,Blueprint
from routes.auth import auth_bp



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)