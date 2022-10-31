from flask import Flask, render_template, url_for, request, current_app
from flask_sqlalchemy import SQLAlchemy
import os

base_dir = os.path.dirname(os.path.realpath(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'users.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)

# db.create_all()
# DB_NAME = "data base.db"


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    country = db.Column(db.String(255))
    gender = db.Column(db.String(10))
    username = db.Column(db.String(50), unique = True, nullable=False)
    email = db.Column(db.String(50), unique = True, index = True, nullable=False)
    password_hash = db.Column(db.String(50))

    def __repr__(self):
        return f"User {self.username}"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/post')
def post():
    return  render_template('/post.html')

@app.route('/editor')
def editor():
    return  render_template('/editor.html')

@app.route('/base')
def base():
    return  render_template('/base.html')

# @app.route('/protected')
# def protected():
    # return  render_template('/protected.html')

@app.route('/sign_up')
def sign_up():
    return  render_template('/sign_up.html')


@app.route('/logout')
def logout():
    pass

# app.app_context()





# app = create_app()

if __name__ == '__main__':
    app.run(debug=True)