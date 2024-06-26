from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    return render_template('login.html', username=name, pwd=password)


if __name__ == '__main__':
    app.run(debug=True)

