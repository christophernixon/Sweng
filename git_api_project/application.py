import json
import csv
import pandas as pd
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
    with open('sampleWeekdays.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        data_list = list()
        for row in reader:
            data_list.append(row)
    data = [dict(zip(data_list[0],row)) for row in data_list]
    data.pop(0)
    s = json.dumps(data)
    return s
# export the final result to a json file

if __name__ == "__main__":
    application.run(debug=True)
