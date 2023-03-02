from django.core.files.storage import default_storage

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
        # Do model logic here

        default_storage.delete(filename)

    return (errno, message)