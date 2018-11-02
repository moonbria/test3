import copy
import os
import random
import base64

import time

import logging
from flask import Flask, jsonify
from flask import make_response
from flask import render_template
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)


app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/nerverthanless'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy()

Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route('/success', methods=["GET", "POST"])
def success():
    with open("successlist.txt", "w") as f:
        f.write(request.url)
    with open("afterstory.txt", "r") as f:
        # f.write("a")
        content = f.readlines()
        i = random.randint(0, 9)
        content = content[i]

    data = {
        "msg": content
    }
    print(content)
    form_csrf_token = request.form.get("csrf_token")
    cookie_csrf_token = request.cookies.get("csrf_token", "")
    print(form_csrf_token, "哈哈哈", cookie_csrf_token)
    if form_csrf_token != cookie_csrf_token:
        data = {
        "msg": "逼我做csrf的坏孩子，咒你一辈子当单身狗"
    }

        return jsonify(data=data)
    print("操作成功")
    # return "转账到%s元到%s成功" % (money, to_account)
    return jsonify(data=data)


@app.route('/')
def hello_world():
    logging.basicConfig(level=logging.WARNING,
                        format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
                        datefmt="%a, %d %b %Y %H:%M:%S",
                        filename="myapp.log",
                        filemode="w")
    li2 = set()
    while len(li2) < 12:
        i = random.randint(1, 59)
        li2.add(i)
    li2 = list(li2)
    li1 = copy.deepcopy(li2)
    i = random.randint(1, 59)
    while i in li1:
        i = random.randint(1, 59)
    li1.append(i)
    for i in li2:
        li1.append(i)
    # random.shuffle(li1)
    li1.sort()
    print(li1)
    print(len(li1))
    data = dict()
    for i in range(25):
        data[i+1] = li1[i]
    print(data)
    csrf_token = generate_csrf()
    response = make_response(render_template("index.html", csrf_token=csrf_token, data=data))
    response.set_cookie("csrf_token", csrf_token)
    return response
    # return render_template("index.html", data=data)

def generate_csrf():
    return bytes.decode(base64.b64encode(os.urandom(48)))

if __name__ == '__main__':
    manager.run()
    # hello_world()