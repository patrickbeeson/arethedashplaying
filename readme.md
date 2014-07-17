# Are the Dash Playing readme

*Author: Patrick Beeson, pbeeson@thevariable.com*

*Copyright The Variable, http://thevariable.com*

## Description

This repository contains the Python Flask application powering the website for arethedashplaying.com.

## Structure

This application has the following structure:

* `arethedashplaying/models.py`: Contains db models for Games and Opponents
* `arethedashplaying/views.py`: Contains views for homepage (single-serving) and 404s
* `arethedashplaying/static`: Contains static assets for css/scss, js and images
* `arethedashplaying/templates`: Contains templates used by various views

## Requirements and dependencies

As listed in `requirements.txt`:

* Babel==1.3
* Fabric==1.8.3
* Flask==0.10.1
* Flask-Babel==0.9
* Flask-SQLAlchemy==1.0
* Jinja2==2.7.2
* MarkupSafe==0.19
* SQLAlchemy==0.9.3
* Werkzeug==0.9.4
* ecdsa==0.11
* itsdangerous==0.23
* paramiko==1.12.3
* pycrypto==2.6.1
* pytz==2014.2
* speaklater==1.3
* wsgiref==0.1.2

As listed in `Gemfile`:

* gem "sass", "~>3.3.10"
* gem "compass", "~>1.0.beta"
* gem "susy"
* gem "breakpoint", "~>2.4.2"

## Instructions

Perform the following steps to run this application locally:

1.  Download or clone the repository to your local computer
2.  Install the requirements (in `requirements.txt` and `Gemfile`)
3.  Run python runserver.py from the drinkthesunshine directory to fire up the Flask development server