# coding=utf-8
from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)


# flask模板
@app.route('/')
def index():
    return render_template('index1.html',  # html里就算{{variable}}在<!--注释-->里也会去识别读取
                           title="<h1>Hello World<h1>",
                           body="## Header22")


# 定义一个模板过滤器，将变量内容，转化成markdown显示
@app.template_filter('md')
def markdown_to_html(txt):
    from markdown import markdown
    return markdown(txt)


# 上下文处理器,这里filename找的是系统的绝对路径
def read_md(filename):
    with open(filename) as md_file:
        content = reduce(lambda x, y: x + y, md_file.readlines())
    return content.decode('utf-8')

@app.context_processor
def inject_methods():
    return dict(read_md=read_md)

if __name__ == '__main__':
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url_delay=True)
