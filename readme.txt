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

20180329
at Terminal tab
>python manager.py dev