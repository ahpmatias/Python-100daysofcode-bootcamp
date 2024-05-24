from flask import Flask, render_template, request, redirect, url_for
from wtforms import StringField, FloatField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Table, Column, MetaData



'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class Base(DeclarativeBase):
  pass



class BookForm(FlaskForm):
    title = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
    submit = SubmitField('Add Book')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
bootstrap = Bootstrap5(app)
all_books = []

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()

@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET','POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        # form_data = {
        #     'title':request.form.get('title'), 
        #     'author':request.form.get('author'), 
        #     'rating':request.form.get('rating')
        #     }
        # all_books.append(form_data)
        with app.app_context():
            new_book = Book(title=request.form.get('title'), author=request.form.get('author'), rating=request.form.get('rating'))
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

