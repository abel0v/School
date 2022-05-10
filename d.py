from flask import Flask
from flask import render_template, url_for
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    dat = []

    for i in range(0, 11 + 1):
        with open(f"static/text_posts/posttitles.txt", 'r', encoding='UTF-8') as f:
            ptitles = f.readlines()
        with open(f"static/text_posts/post{i + 1}.txt", 'r', encoding='UTF-8') as f:
            ptext = f.read(222)
        dat.append((ptitles[i], f'/static/img/img{i}.jpeg', ptext, i))
    return render_template('index.html', data=dat)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/post/<int:postnum>')
def viewpost(postnum):
    img = postnum
    with open(f"static/text_posts/post{postnum + 1}.txt", 'r', encoding='UTF-8') as f:
        t = f.read()
    with open(f"static/text_posts/posttitles.txt", 'r', encoding='UTF-8') as f:
        ptitles = f.readlines()
    return render_template('post.html', title=ptitles[postnum], item=img, text=t)


@app.route('/raspis')
def raspiss():
    return render_template('rasp.html')


@app.route('/items')
def print_items():
    db = sqlite3.connect('classes.db')
    cursor = db.cursor()
    data = list(cursor.execute("""SELECT id, class, name, surname, profcl FROM pupules""").fetchall())
    for i in range(len(data)):
        data[i] = list(data[i])
    for i in data:
        i[4] = cursor.execute(f"""SELECT prof FROM profiles WHERE id={i[4]}""").fetchall()[0][0]
    return render_template('print_items.html', items=data)


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
