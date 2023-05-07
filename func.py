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
names = ['joy', 'henry', 'mark','job'] 
con = {'subject':'maths','age':45} 
info(*names,**con) 
# Example of function 
days_in_the_month =[0,31,28,31,30,31,30,31,31,30,31,30,31] 
def leap_year(year): 
    return year % 4 ==0 and (year % 100 != 0 or year %100 == 0) 

print(leap_year(2017))     
print(leap_year(2020))
    
def num_of_days(year,month): 
    if not 1 <= month <= 12: 
        return 'invalid' 
    if month ==2 and leap_year(year):
        return 29 
    
    return days_in_the_month[month] 

print(num_of_days(2020,2))
print(num_of_days(2045,25))
