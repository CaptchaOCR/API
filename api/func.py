from django.core.files.storage import default_storage

from CaptchaOCR.CNN.run_model import run_model 

def run_model(filename):

    errno = 0
    message = ""

    if(filename == None):
        errno=1
        message="No filename specified"

    elif(not default_storage.exists(filename)):
        errno=1
        message="Could not find " + filename

    else:
        file = default_storage.open(filename, mode='r')

        # Model logic
        try:
            message = run_model(filename)
        except Exception as e:
            errno = 1
            message = 'Run model unsuccessful:\n', e

        default_storage.delete(filename)

    return (errno, message)
