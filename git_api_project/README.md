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

### Which is the most popular day to commit code?
This is the question I intend to answer. To figure this out, I need the amount of commits per day, for some reasonable timespan. To run this query on every repository in github would take a very long time, so for a POC I will limit myself to one large repository first: I have chosen the [Apache Spark repository](https://github.com/apache/spark). As of writing this has about 25,000 commits. I will extract out the day that each commit was committed on and aggregate these to get totals for each day. 