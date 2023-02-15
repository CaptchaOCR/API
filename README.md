# CaptchaOCR API
This repository is the backend for CaptchaOCR. It requires a trained model to run, please see the [CNN Repository](https://github.com/CaptchaOCR/API) for training.  


## Installation
To install for development:

### MacOS and Linux

1. Make sure python is installed.  
`python3 --version`

2. Create a python virtual environment.  
`python3 -m venv NNEnvironment`

3. Activate the CNN virtual environment.  
`source ./NNEnvironment/bin/activate`

4. Install the dependencies for NNEnvironment.  

    a. For machines with discrete GPUs (Graphics Cards):  
`pip install -r ./requirements_CUDA.txt`

    b. For machines without:  
`pip install -r ./requirements.txt`

### Windows

1. Make sure python is installed.  
`py --version`

2. Create a python virtual environment.  
`py -m venv NNEnvironment`

3. Activate the CNN virtual environment.  

    a. For Command Line:  
`.\NNEnvironment\Scripts\activate.bat`

    b. For PowerShell:  
`.\NNEnvironment\Scripts\activate.ps1`

4. Install the dependencies for NNEnvironment.  

    a. For machines with discrete GPUs (Graphics Cards):  
`pip install -r ./requirements_CUDA.txt`

    b. For machines without:  
`pip install -r ./requirements.txt`


## Run
Instructions to run the server will come soon.

1. Run the virtual environment.

    a. For macOS and Linux:  
`source ./NNEnvironment/bin/activate`

    b. For Windows:  
`.\NNEnvironment\Scripts\activate.bat`

2. Train the nerual network.  
`python manage.py runserver`