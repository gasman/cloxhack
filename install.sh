#!/bin/sh

sudo apt-get install -y python-dev libasound-dev python-pip supervisor
git clone https://github.com/superquadratic/rtmidi-python.git
cd rtmidi-python
python setup.py build
cd ..
cp rtmidi-python/build/lib.linux-armv6l-2.7/rtmidi_python.so .

sudo pip install virtualenvwrapper
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv cloxhack
pip install -r requirements.txt

sudo cp cloxhack-supervisor.conf /etc/supervisor/conf.d/cloxhack.conf
