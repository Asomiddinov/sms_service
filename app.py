import os
from http import client
from flask import Flask, request, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
csrf = CSRFProtect(app)

# Flask-WTF requires an encryption key - the string can be anything:
app.config['SECRET_KEY'] = "asdfsadfsdf"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://nlmduvnodvvxhz:2ca79b8a3092290d38a6b27e5d5cfc504c8f74a5245cff0fe0ecd807499bf093@ec2-3-229-252-6.compute-1.amazonaws.com:5432/d711f5638ti7as"
Bootstrap(app)


class NamerForm(FlaskForm):
    name = StringField(
        "What's the phone number you want to send?", validators=[DataRequired()])
    body_text = TextAreaField("Body text", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/name", methods=["GET", "POST"])
def name():
    account_sid = 'ACefbcbf4c94234feb0f8a6ec85ff63292'
    auth_token = '20eb76bcbef3f22a8d1f4e1570e80ae2'
    name = None
    body_text = None
    form = NamerForm()
    client = Client(account_sid, auth_token)
    # Validate form:
    if form.validate_on_submit():
        name = form.name.data
        body_text = form.body_text.data
        form.name.data = ""
        form.body_text.data = ""
        client.messages.create(to=str(name),
                               from_="+19378843082",
                               body=str(body_text))
    return render_template("name.html", name=name, body_text=body_text, form=form)


if __name__ == "__main__":
    app.run(debug=1)
