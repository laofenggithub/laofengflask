20171220
study flask
*mac python path /System/Library/Frameworks/Python.framework/Versions

*install pip
mac
1.download get-pip.py
2.$sudo python get-pip.py

ubuntu
$sudo apt-get install python-dev python-pip

*change pip source
$cd ~
$mkdir .pip
$touch pip.conf
$vi pip.conf
    [global]
    index-url=http://mirrors.aliyun.com/pypi/simple/
    [install]
    trusted-host=mirrors.aliyun.com

*install falsk
$pip install flask
maybe use
$sudo pip install falsk

*install virtualenv
$sudo apt-get install virtualenv

*use virtualenv
$mkdir myproject
$virtualenv venv
$. venv/bin/activate
20171221
*pip all package to txt,install all package in txt
$pip freeze > requirement1221.txt
$pip install -r requirement1221.txt
*reload to mypage for [live_server = Server(app.wsgi_app)]
$python xxx.py

20180207 logarithms
问题1:注册功能报错。
前台显示：Internal Server Error
The server encountered an internal error and was unable to complete your request.
Either the server is overloaded or there is an error in the application.
后台显示：
 File "/Users/fengshuai/myflaskenv/lib/python2.7/site-packages/sqlalchemy/orm/events.py", line 1889, in wrap
    fn(target, value, *arg)
TypeError: on_created() takes exactly 3 arguments (4 given)
[E 180207 22:40:14 wsgi:355] 500 POST /auth/register (127.0.0.1) 28.45ms
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

20180329
at Terminal tab
laofengflask>python manager.py dev
