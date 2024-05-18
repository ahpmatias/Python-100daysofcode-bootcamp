from flask import Flask, render_template, request
import requests
import smtplib
import os

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.get("/contact")
def contact():
    initial_heading = 'Contact Me'
    return render_template("contact.html", heading=initial_heading)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

personal_email = os.environ.get('EMAIL')
personal_pwd = os.environ.get('PASSWORD')

@app.post('/contact')
def receive_data():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= personal_email, password= personal_pwd)
        connection.sendmail(from_addr=personal_email,
                            to_addrs=personal_pwd,
                            msg=f"Name: {name}\n Email: {email}\n Phone: {phone}\n Message: {message}")

    success_heading = 'Successfully sent your message.'
    return render_template('contact.html', heading=success_heading)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
