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
        
        
            
        