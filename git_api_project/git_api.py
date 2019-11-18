import json
import logging

import keyring
from github import Github


def get_user_info(user):
    """Given a user, attempts to find a token for that user
    in local keychain, if sucessfull returns the GET /user json response."""
    token = keyring.get_password('github', user)
    if token == None:
        logging.error("No token set for user: %s",user)
        return
    github = Github(token)
    return github.get_user().raw_data

if __name__ == "__main__":
    user = 'christophernixon'
    print(get_user_info(user))
