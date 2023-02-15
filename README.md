# CaptchaOCR API
This repository is the backend for CaptchaOCR. It requires a trained model to run, please see the [CNN Repository](https://github.com/CaptchaOCR/API) for training.  


## Installation
To install for development:

### MacOS and Linux

1. Make sure python is installed.  
`python3 --version`

2. Create a python virtual environment.  
`python3 -m venv CaptchaOCR-API`

3. Activate the CNN virtual environment.  
`source ./CaptchaOCR-API/bin/activate`

4. Install the dependencies for CaptchaOCR-API.  
`pip install -r ./requirements.txt`

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

4. Install the dependencies for CaptchaOCR-API.  
`pip install -r ./requirements.txt`


## Run
Instructions to run the server.

1. Run the virtual environment.

2. Make migrations.  
`python manage.py migrate`

3. Run the server.  
`python manage.py runserver`