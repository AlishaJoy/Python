#functions:

def abc():
    pass

print(abc())
# functions with empty brackets
def ab():
    print("hi im ab function")
    
ab() 
# calling same function in a loop
for i in range(4):
    ab()
    
# function with return type 
def b():
    return 'hello'
    
print(b())
print(b().upper())
print(len(b())) 

# passing parameter to a function:

def par(parameter):
    return '{}'.format(parameter)

print(par("i am the parameter"))

def mpar(hey,hello):
    return '{} I am {}!'.format(hey,hello)

print(mpar('hey','john'))

# *args takes positional arguments, **kwargs takes keyword arguments
def info(*args, **kwargs):
    print(args)
    print(kwargs)
 
info('hello everyone','nice to meet you all','Im', name = 'julie',age = 25)    
  
# with list 
 

