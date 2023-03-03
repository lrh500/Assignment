# assignment
#The description of this application
This application is a Flask web application that uses the Jinja2 template engine work on Render, a cloud hosting service, which shows the movies and the ratings from users.
The URL of render:https://assignment-apx5.onrender.com

#Prerequisites

Before you start, you need the following:

A working Flask application that uses Jinja2 templates
A virtual environment set up for your Flask application

#The pakage that this application need
app==0.0.1
async-generator==1.10
attrs==22.2.0
behave==1.2.6
certifi==2022.12.7
exceptiongroup==1.1.0
gunicorn==20.1.0
h11==0.14.0
idna==3.4
outcome==1.2.0
parse==1.19.0
parse-type==0.6.0
PySocks==1.7.1
selenium==4.8.2
six==1.16.0
sniffio==1.3.0
sortedcontainers==2.4.0
trio==0.22.0
trio-websocket==0.9.2
typing-extensions==4.5.0
urllib3==1.26.14
wsproto==1.2.0
Jinja2==2.11.3
Flask==1.1.4
markupsafe==1.1.1

#How to run 
pyenv local 3.7.0 # this sets the local version of python to 3.7.0 
python3 -m venv .venv # this creates the virtual environment for you source .venv/bin/activate # this activates the virtual environment 
pip install --upgrade pip # package installer for python
pyenv install 3.7.0 #Installs version 3.7.0 into environment for use in global or local system
#Parameters to start
export FLASK_APP=Framework.py
export FLASK_ENV=development
python3 –m flask run –host 0.0.0.0 # if the server works on codio

#How to use
The home page has 2 links, which links to movies page and ratings page, the ratings page shows all ratings from users. If you want to see the rating of one of movies, click into movies page, then click the movie id that you want to see, which could show all the rating from different users for same movie.



