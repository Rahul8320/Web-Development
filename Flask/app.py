from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)

# configure our database uri
app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']

db = SQLAlchemy(app)

# basic model
class Contact(db.Model):
    __tablename__ = 'Contact'
    '''slNo name email phone msg postTime'''
    slNo = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    postTime = db.Column(db.String(120), nullable=False)


class Posts(db.Model):
    __tablename__ = 'Posts'
    '''slNo title content postBy postTime slug imgFiles'''
    slNo = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    postBy = db.Column(db.String(255), nullable=False)
    postTime = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(55), nullable=False)
    imgFiles = db.Column(db.String(55), nullable=False)

@app.route("/")
def home():
    posts = Posts.query.filter().all()
    return render_template('index.html',posts=posts)

@app.route("/dashboard")
def login():
    return render_template('login.html')

@app.route("/about")
def about():
    return render_template('about.html',params=params)

@app.route("/post/<string:post_slug>", methods=['GET'])
def post(post_slug):
    post_data = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', posts=post_data)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        # add entry to database
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        if len(name) == 0 and len(email) == 0 and len(phone) == 0:
            return render_template('contact.html')
        entry = Contact(name=name,email=email,phone=phone,msg=message,postTime=datetime.now())
        db.session.add(entry)
        db.session.commit()

        return render_template('thank.html')

    else:
        return render_template('contact.html')


app.run(debug=True)

