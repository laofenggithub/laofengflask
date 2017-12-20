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
 