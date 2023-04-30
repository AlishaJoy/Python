#if else elif

a = 'joy'

if a == 'joyful':
    print('it is equal joyful')
elif a == 'joy' :
    print("it is equal to joy")  
elif a == 'welcome':
    print("it is equal to welcome") 
else:
    print("not equal")
    
    
b = 'happy'
c = 'new year'

if a == 'happy' and c =='new year':
    print('happy new year!!')
elif a == 'happy' or c == 'new year': 
    print("happy new year!")
elif not c:
    print('oo')
else :
    print("not matched")               
      

r = [10,20,30]
t = [10,20,30] 

print(id(r))
print(id(t))
print(r is t)
print(r == t)     
print(id(r) != id(t))


#checking true conditions
 
pop =  0

if pop :
    print("it is true")
else :
    print("it is false")
        
#other fasle conditions are:
# False #None # empty sequence ' ', (), { }, []

op = 'hello'

if op :
    print("true")
else :
    print("false")    
#other true conditions :
# numerical values
