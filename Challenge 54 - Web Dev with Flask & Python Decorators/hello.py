from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/bye')
def say_bye():
    return '<h1>Bye!</h1>'

if __name__ == '__main__':
    app.run()

# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#
#     return wrapper_function()
#
# @delay_decorator
# def say_hello():
#     print('hello!')
#
# @delay_decorator
# def say_bye():
#     print('bye!')
