#coding=utf-8
import os
from flask import Flask,request,redirect,url_for,send_file,render_template
from write_poem import WritePoem,start_model

app = Flask(__name__)
application = app

path = os.getcwd()    #获取当前工作目录
print(path)

writer = start_model()

@app.route('/')
def index():
    return 'test ok'

#sytle_help = '<br> 诗歌类型 :<br> <button id=\'1\' >1:自由诗</button><br> <button id=\'2\'>2:带押韵的自由诗</button><br> <button id=\'3\'>3:藏头诗</button><br><button id=\'4\'>4:给定若干字，以最大概率生成诗</button>'

@app.route('/poem')
def write_poem():
    params = request.args
    start_with= ''
    poem_style = 0

    # print(params)
    if 'start' in params :
        start_with = params['start']
    if 'style' in  params:
        poem_style = int(params['style'])

    # return 'hello'
    if  start_with:
         if poem_style == 3:
            return  writer.cangtou(start_with)
         elif poem_style == 4:
            return writer.hide_words(start_with)

    if poem_style == 1:
        return  writer.free_verse()
    elif poem_style == 2:
        return writer.rhyme_verse()

    return send_file("index.html")


if __name__ == "__main__":
    app.run()