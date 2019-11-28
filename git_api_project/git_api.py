import json
import logging
import keyring
from github import Github
from datetime import date
import dateutil.parser
import calendar

def get_weekday_commit_freq(repo,user=''):
    """Given a repository, this uses the github api to search for this repository,
    and returns an array containing the counts of commits on each day for the first search result.
    User parameter is optional, the github api allows more authenticated requests per hour."""
    return format_raw_commit_data(get_commits(repo,user))

def get_commits(repo,user=''):
    """Searches for a particular repository using the search github API,
    then returns all commits of the first repo."""

    # Attempting to use authenticated requests.
    token = keyring.get_password('github', user)
    if token == None:
        github = Github()
        logging.debug("No token set for user: %s",user)
    else:
        github = Github(token)
    
    top_search_results = github.search_repositories(query=repo)
    top_repo = top_search_results[0]
    return top_repo.get_commits()
    

def format_raw_commit_data(commits):
    """Given a Paginated List of commits for a particular repository, this iterates through all the commits
    and returns an array contain the count of commits for each day of the week."""

    # Setting up a frequency dict
    weekday_freq = {'Monday':0,
                    'Tuesday':0,
                    'Wednesday':0,
                    'Thursday':0,
                    'Friday':0,
                    'Saturday':0,
                    'Sunday':0}

    for commit in commits:
        date = commit._rawData['commit']['author']['date']
        date_object = dateutil.parser.parse(date)
        weekday = calendar.day_name[date_object.weekday()]
        if weekday in weekday_freq:
            weekday_freq[weekday] += 1
        else:
            weekday_freq[weekday] = 1

    # Formatting frequency dict into array
    return_array = []
    for weekday in weekday_freq:
        tmp_dict = {'weekday':weekday, 'commits': weekday_freq[weekday]}
        return_array.append(tmp_dict)

    return return_array
