import json
import csv
import logging
import pandas as pd
from git_api import git_api
from flask import (Flask, abort, flash, jsonify, redirect, render_template,
                   request, send_file, send_from_directory, session)

#1. Declare application
application=Flask(__name__)

#2. Declare data stores
class DataStore():
    CountryName=None
    Year=None
    Prod= None
    Loss=None
data=DataStore()

@application.route("/main",methods=["GET","POST"])

#3. Define main code
@application.route("/",methods=["GET","POST"])
def homepage():
    return render_template("index.html")

@application.route("/weekday_data",methods=["GET","POST"])
def handle_weekday_data_request():
    # This is to allow for authenticated api requests
    user = 'christophernixon'

    if request.method == 'POST':
        repo = request.json.get('repo')
    else:
        # Since it is a GET request, the default repository data is supplied. 
        repo = 'sweng'
    try:
        api = git_api(repo, user)
        weekday_data = api.get_weekday_commit_freq()
        return json.dumps(weekday_data)
    except AttributeError as e:
        logging.error(e)
        abort(400)

@application.route("/apache-data",methods=["GET","POST"])
def returnApacheData():
    try:
        with open('/Users/chrisnixon/yr3/sweng/git_api_project/static/apacheWeekdays.json', 'r') as f:
            data = json.load(f)
        return json.dumps(data)
    except Exception as e:
        logging.error(e)
        abort(400)

@application.route("/nodejs-data",methods=["GET","POST"])
def returnNodeJsData():
    try:
        with open('/Users/chrisnixon/yr3/sweng/git_api_project/static/nodejsWeekdays.json', 'r') as f:
            data = json.load(f)
        return json.dumps(data)
    except Exception as e:
        logging.error(e)
        abort(400)

@application.route("/flutter-data",methods=["GET","POST"])
def returnFlutterData():
    try:
        with open('/Users/chrisnixon/yr3/sweng/git_api_project/static/flutterWeekdays.json', 'r') as f:
            data = json.load(f)
        return json.dumps(data)
    except Exception as e:
        logging.error(e)
        abort(400)

@application.route("/typescript-data",methods=["GET","POST"])
def returnTypescriptData():
    try:
        with open('/Users/chrisnixon/yr3/sweng/git_api_project/static/typescriptWeekdays.json', 'r') as f:
            data = json.load(f)
        return json.dumps(data)
    except Exception as e:
        logging.error(e)
        abort(400)

if __name__ == "__main__":
    application.run(debug=True)
