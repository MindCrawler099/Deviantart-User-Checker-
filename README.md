# A SIMPLE DEVIANTART USER CHECKER

### About
* This is an app built in python.
* It is constructed in a venv virtual environment

### Setting up project environment
* Clone the repository
* Create a venv virtual environment in the project folder using the following commands
```Bash
    py -m venv env
    source ./env/Scripts/activate
    pip install requirements.txt -y
```
* If internet connection is avaliable, the requests and bs4 modules will be installed

### How to use
* A **valid** deviantart username is entered into the 'username' field
* Click on the 'Check Details' button
* If the account and entered username are both still valid, the details should appear
* If the username is not valid, the account is taken down or internet connection is unavaliable, an error will be thrown