from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), validators.Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), validators.Length(min=8)])
    submit = SubmitField(label='Login')

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = "thatwashardenough"

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.get('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
    
@app.post('/login')
def validate():
    form = LoginForm()
    if form.validate_on_submit() and form.email.data == 'admin@email.com' and form.password.data == '12345678':
        return render_template('success.html', form=form)
    else:
        return render_template('denied.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)
