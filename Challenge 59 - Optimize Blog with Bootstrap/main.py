from flask import Flask, render_template
import requests

app = Flask(__name__)

endpoint = 'https://api.npoint.io/70d21c094353f5b6437d'
response = requests.get(endpoint)
all_posts = response.json()

@app.route('/')
def home():
    home_heading = "Anderson's Blog"
    home_subheading = "Don't mind me, just learning some Web Dev."
    home_bg_img = 'home-bg.jpg'
    return render_template('index.html', page_heading=home_heading, bg_image=home_bg_img,
                           posts=all_posts, page_subheading=home_subheading)


@app.route('/about')
def about():
    about_heading = 'About Me'
    about_subheading = 'This is what I do.'
    about_bg_img = 'about-bg.jpg'
    return render_template('about.html', page_heading=about_heading, page_subheading=about_subheading,
                           bg_image=about_bg_img)


@app.route('/contact')
def contact():
    contact_heading = 'Contact Me'
    contact_subheading = 'Have questions? I have answers.'
    contact_bg_img = 'contact-bg.jpg'
    return render_template('contact.html', page_heading=contact_heading,
                           page_subheading=contact_subheading, bg_image=contact_bg_img)


@app.route('/post/<post_id>')
def post(post_id):
    post_id = int(post_id)
    post_bg_img = f'post_bg_{post_id}.jpg'
    return render_template("post.html", post_id=post_id, posts=all_posts, bg_image=post_bg_img)


if __name__ == '__main__':
    app.run(debug=True)