from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    my_name = 'Anderson'
    year = dt.datetime.now().year
    return render_template('index.html', num=random_number, CURRENT_YEAR=year, NAME=my_name)


@app.route('/guess/<name>')
def guess(name):
    agify_url = 'https://api.agify.io'
    agify_response = requests.get(f'{agify_url}?name={name}').json()['age']
    genderize_url= 'https://api.genderize.io'
    genderize_response = requests.get(f'{genderize_url}?name={name}').json()['gender']
    return render_template('guess_name.html', name=name, age=agify_response, gender=genderize_response)


@app.route('/blog/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)


