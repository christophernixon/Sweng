import json
import csv
import pandas as pd
import git_api
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

@application.route("/get-data",methods=["GET","POST"])
def returnProdData():
    # Get commits from repo
    repo = 'sweng'
    user = 'christophernixon'
    try:
        commits = git_api.get_commits(repo,user)
        return json.dumps(commits)
    except Exception as e:
        print(e)
        
@application.route("/search-repos",methods=["GET","POST"])
def returnSearchData():
    # Get commits from repo
    repo = request.json.get('repo')
    print(repo)
    user = 'christophernixon'
    try:
        commits = git_api.get_commits(repo,user)
        return json.dumps(commits)
    except Exception as e:
        print(e)
    return

@application.route("/apache-data",methods=["GET","POST"])
def returnApacheData():
    with open('/Users/chrisnixon/yr3/sweng/git_api_project/apacheWeekdays.json', 'r') as f:
        data = json.load(f)
    return json.dumps(data)

@application.route("/nodejs-data",methods=["GET","POST"])
def returnNodeJsData():
    with open('/Users/chrisnixon/yr3/sweng/git_api_project/nodejsWeekdays.json', 'r') as f:
        data = json.load(f)
    return json.dumps(data)

@application.route("/flutter-data",methods=["GET","POST"])
def returnFlutterData():
    with open('/Users/chrisnixon/yr3/sweng/git_api_project/flutterWeekdays.json', 'r') as f:
        data = json.load(f)
    return json.dumps(data)

@application.route("/typescript-data",methods=["GET","POST"])
def returnTypescriptData():
    with open('/Users/chrisnixon/yr3/sweng/git_api_project/typescriptWeekdays.json', 'r') as f:
        data = json.load(f)
    return json.dumps(data)

if __name__ == "__main__":
    application.run(debug=True)
