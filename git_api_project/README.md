Dependencies are in 'requirements.txt'.

Install with 
``` 
pip install -r requirements.txt 
```

### Secrets
Secrets are stored in the keychain, through the use of the 'keyring' library.
To set a secret use:
``` 
keyring set SERVICE USERNAME
```
There will then be a prompt for inputting the secret. 

### Outline
1) Figure out which visualisation will be used first. 
2) Which data will be needed for that visualisation.
3) Build json sample for the visualisation. Create a sample json first for working on the visualisation.

### Architecturally 
- A module for extracting and processing data, perhaps from a given repository name. This will use the github api, and extract the necessary data from the api requests. It will then store this information in some kind of database.
- Database. This will recieve information from data-extraction module. Need to figure out what kind of database I need. The data in the database needs to be of the format that it can be extracted and directly used by the d3 visualisation. Alternatively, the data could be pushed into the database and SQL queries coudl be used to extract and format the correct data.
- Server. A web server which can take information from a database(potentially using SQL queries). This will then serve a html/javascript bit of code which will have the visualisations. 

### MISC Notes
Potential questions: Which day of th eweek is the best code written? Which day do most open-source developers commit code?
Most used languages in the last week?
Where do most developers live?(Potentially using timestamps, and a visualisation with timezones)