# make a list of names 
names = ['joy','reni','reshma','bindhu']
fruits = ['pine','mango','apple']
nums = [33,55,22,6,1,88]

print(names)
print(len(names))
print(names[2])
print(names[:3])
print(names[2:])

#modifying list 

names.append("jeena")
names.insert(0,"ben")
print(names)

names.insert(3,fruits)
print(names)
names.extend(fruits)
print(names)

names.remove("reni")
print(names)

names.pop()
names.pop()
names.pop()
print(names)

names.reverse()
print(names)

fruits.sort()
print(fruits)

nums.sort()
print(nums)

#if you wanna reverse sort

nums.sort(reverse = True)
print(nums)

#if you dont want to alter the original list and make a copy of sorted list
#use sorted() function instead of sort method
new_list = sorted(nums)
print(new_list)

#minimum and maximum
print(min(nums))
print(max(nums))
print(sum(nums))

#find the index of the list item

print(names.index('joy'))

#check if the item is present or not 
print('old' in names)
print('bindhu' in names)

#print all variables with for 

for all_names in names:
    print(all_names)
    
#print the index of item and its name use enumerate() function

for index,all_names in enumerate(names):
    print(index,all_names)
    
new = '---'.join(fruits)
print(new)         

back = new.split('---')
print(back)