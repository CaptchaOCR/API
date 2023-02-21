# CaptchaOCR API
This repository is the backend for CaptchaOCR.  
It requires a trained model to run, please see the [CNN Repository](https://github.com/CaptchaOCR/API) for training.  


## Installation
To install for development. Initial setup for the virtual environment is different depending on which OS you are using. Afterwards, the instructions are the same:

### MacOS and Linux

1. Create a python virtual environment.  
`python3 -m venv CaptchaOCR-API`

2. Activate the CNN virtual environment.  
`source ./CaptchaOCR-API/bin/activate`

### Windows

1. Make sure python is installed.  
`py --version`

2. Create a python virtual environment.  
`py -m venv CaptchaOCR-API`

3. Activate the CNN virtual environment.  

    a. For Command Line:  
`.\CaptchaOCR-API\Scripts\activate.bat`

    b. For PowerShell:  
`.\CaptchaOCR-API\Scripts\activate.ps1`


### Setup
After creating the virtual envrionment, the steps for both OS's are the same.

4. Install the dependencies for CaptchaOCR-API.  
`pip install -r ./requirements.txt`

5. Set Django's secret key. (This is only important for deployment)  
`dotenv set SECRET_KEY <value>`

## Run
Instructions to run the server.

1. Activate the virtual environment.

2. Make migrations.  
`python manage.py makemigrations && python manage.py migrate`

3. Run the server.  
`python manage.py runserver`

## Deploy
Deployment instructions coming soon.