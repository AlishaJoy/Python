# for loop
num = [10,20,30,40,60]

for i in num:
    print(i)
    
#break and continue 

for i in num:
    if i==30:
        print('found 30')
        break
    print(i)
    
for j in num:
    if j == 30:
        print('found 30')
        continue 
    print(j)

#loop within a loop 

for i in num:
    for eachletter in 'pqr':
        print(i,eachletter)
        
#for a loop till a range 
for i in range(5):
      print(i)

for i in range(1,3):
    print(i)
    
#while loops  -- until certain condition is met

e = 0
while e<8:
    if e == 5:
        break
    print(e)
    e +=1 
 
f = 0
while True:
    if f == 4:
        break
    print(e)
    e += 1
    
    
    

    
               
        
            
        