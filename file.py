
f = open('test.txt')
f = open('test.txt', 'r')
print(f.name)
print(f.mode)
f.close()

#using context manager :
with open('test.txt','r') as f:
    contents = f.read()
    print(contents)
    
