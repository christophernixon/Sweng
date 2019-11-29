
# Software Engineering Project
Visualising data from the Github API using D3.

![image](./misc/sweng_app.png)

This visualisation should be hosted [here](https://sweng-app-heroku.herokuapp.com/).

## Which is the most popular day to commit code?
This is an attempt to visually represent the most popular day to commit code. To demonstrate this I chose to use a Circular Packing chart from D3. This assigns a different colored circle to each day, and I have scaled the size of the circles to correspond to the amount of commits for that day. 

## Using the visualisation
This graph works on a single repository at a time, above the graph is an information panel which shows some details about the selected repository. Upon loading the page there is some default data loaded into the graph. On the right hand panel there is a feature for searching for a different repository. This works well for smaller repositories but due to [technical issues](#Technical\ Issues), it takes a long time to load larger repositories. 

Below this are buttons to select a few pre-loaded large repositories, so you can see what the graph looks like with a larger dataset without having to wait a long time. 

## Running locally
Dependencies are in 'requirements.txt'. These can be installing using pip by running the following from the root directory:
```
pip install -r requirements.txt 
```
The application can then be run, again from the main directory:
```
python main.py
```

## Technical Issues

This graph requires information on every commit to a repository, and on large repositories this requires a lot of calls to the github API, since only 30 commits are supplied per api call.

Partially stemming from this heavy usage of the github API is the issue of authenticated requests. Github has hourly rate-limiting on requests: as of writing 60 for unauthenticated requests, 5000 for authenticated requests.

### Authenticating requests
The app will attempt to create an authenticated session using a github username and personal access token, details for generating one [here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line).
These access tokens are stored in the keychain, through the use of the 'keyring' library.
To set a secret(token) use:
``` 
keyring set github USERNAME
```
There will then be a prompt for inputting the token. If no token is set, unauthenticated requests will be used instead. 

