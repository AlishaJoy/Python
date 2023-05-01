#lists are mutable and tuples are not mutable
# we cannot append, remove or anything with the tuples

colors = ('red','black','blue' )
col = colors
print(colors)
print(col)

#the below shows an error
#colors[2] = 'green'
#print(colors)
#print(col)


#sets 
#they are  values that are unordered
veg ={ 'potato', 'tomato', 'carrots'}
vegg = {'beans', 'gaurd','tomato'}
print(veg)

print(veg.intersection(vegg))
print(veg.difference(vegg))
print(veg.union(vegg))

#create an empty
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {}
empty_set = set()


