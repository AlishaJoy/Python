print('i am the to be imported folder')

def index(list , target):
    for i , value in enumerate(list):
        if value == target:
            return i
        
    return -1
