from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email
import logging

app = Flask(__name__)


class EmailLoginForm(Form):
    username = StringField('username', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['post'])
def login():
    form = EmailLoginForm()
    if form.username.data == "alicia@test.se" and form.password.data == "secret": #can add/check whether this user name exist in the database
        return render_template('login_success.html')
    else:
        return render_template('login_failure.html')


if __name__ == '__main__':
    app.logger.setLevel(logging.DEBUG)
    app.config['SECRET_KEY'] = 'any secret string'
    app.run()