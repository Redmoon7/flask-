import os
from flask import Flask, render_template, request, session, redirect, jsonify

from Data import Data

app = Flask(__name__,
            static_folder='templates/static'
            )


def DictUrl(s):
    s = s[1:-1]
    pairs = s.split(',')
    my_dict = {}

    for i in pairs:
        key, value = i[:1], i[2:]
        my_dict.update({
            key: value
        })

    return my_dict

@app.route('/', methods=['GET'])
def index():

    return '你好这里是首页'

@app.route('/api/data/<id>', methods=['GET'])
def get_data(id):
    # 处理请求并获取数据
    Name, ImageUrl, Position, Birthday, URL = Data().CheckAll(Name=id)
    Js = {
        'id': Name,
        'ImageUrl': ImageUrl,
        'Duties': Position,
        'Birthday': Birthday,
        'URL': DictUrl(URL)
    }

    return jsonify(Js)


if __name__ == '__main__':
    app.run(debug=True, port=8888)
