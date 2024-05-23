from flask import Flask, render_template, request, redirect, url_for
from wtforms import StringField, FloatField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5


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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)
all_books = []

class BookForm(FlaskForm):
    title = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
    submit = SubmitField('Add Book')


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET','POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        print('True')
        print(request.form.get('title'))
        print(request.form.get('author'))
        form_data = {'title':request.form.get('title'), 'author':request.form.get('author'), 'rating':request.form.get('rating')}
        all_books.append(form_data)
        print(all_books)
    else:
        print('False')
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

