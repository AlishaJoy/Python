# dictionary
# key value pairs, key is a unique identifier where we can find our data,and the value is our data

info = { 'name':'henry', 'age': 30, 'courses' :['math','science']}
# befire the colon is key , after the colon is value
print(info)
print(info['name'])
print(info['courses'])

#key if doesn't exist
#print(info('hey'))         # prints error

print(info.get('hey'))      #prints none
print(info.get('hello','not found!!'))  #prints not found!!

# add new entry
info['phone'] ='9489888988'
info['name']= 'john'
print(info)

# using update method
info.update({'name':'amy','age':'77'})
print(info)
 
# delete 
del info['age']
print(info)

# delete using pop
i = info.pop('name')
print(info)
print(i)

print(len(info))
print(info.keys())
print(info.values())
print(info.items())

for key,value in info.items():
    print(key,value)
    



