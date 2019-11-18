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
