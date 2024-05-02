from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route('/')
def guess_number():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')


@app.route('/<number>')
def check_number(number):
    if int(number) > random_number:
        return ('<h1 style="color:purple">Too high, try again!</h1>'
                '<img src="https://media.giphy.com/media/l1KVaj5UcbHwrBMqI/giphy.gif?cid=790b761118q6jb27ca6chlihrj46'
                'hjs2tcwsotus8pd7pb0k&ep=v1_gifs_search&rid=giphy.gif&ct=g">')

    if int(number) < random_number:
        return ('<h1 style="color:red">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMThxNmpiMjdjYTZjaGxpaHJqNDZoanMydGN3c290'
                'dXM4cGQ3cGIwayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/OPU6wzx8JrHna/giphy.gif">')

    if int(number) == random_number:
        return ('<h1 style="color:green">You found me!</h1>'
                '<img src="https://media.giphy.com/media/6MWahPArixa6I/giphy.gif?cid=790b7611ufge5xua8sa8wukjmtqed0b'
                'myhi6nmtpuu3u3eeb&ep=v1_gifs_search&rid=giphy.gif&ct=g">')


if __name__ == '__main__':
    app.run(debug=True)
