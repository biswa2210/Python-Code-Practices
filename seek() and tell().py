f=open("biswa.txt")
print(f.tell())#return current position of file
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
f.seek(11)#reset file pointer at 11 position
print(f.read())