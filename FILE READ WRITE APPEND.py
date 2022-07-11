f=open("biswa.txt","w")#open in write mode
f.write("HELLO I AM BISWA,IT IS MY 1ST FILE IN PYTHON.")
f.close()
#f=open("biswa.txt","r")----->open in read mode
#print(f.read())
#f.close()
f=open("biswa.txt","a")#open in append mode
f.write("\nI WANT TO BE A BEST PROGRAMMAR IN THIS WORLD....")
f.close()
#f=open("biswa.txt","r")#open in read mode
#print(f.read())
#f.close()
f=open("biswa.txt","w")#open in write mode
f.write("HELLO I AM BISWA...")
f.close()
f=open("biswa.txt","r")
#print(f.read())
f.close()
f=open("biswa.txt","r+")#READ AND WRITE BOTH
content=f.read()
#print(content)
f.write("HELLO I AM BISWARUP...")
f.close()
f=open("biswa.txt","r")
print(f.read())
f.close()
f=open("biswa.txt","w")#open in write mode
A=f.write("HELLO I AM BISWARUP....")#NO OF CHARACTERS FOR WRITING
f.close()
print(A)
f=open("biswa.txt","r")
print(f.read())
f.close()
f=open("biswa.txt","a")#open in append mode
f.write("\nI want to be a good programmar\nMy favourite language is python...")
f.close()
with open("biswa.txt") as f:
    value=f.read(5)
    print(value)
f=open("biswa.txt")
print(f.readlines())
f.close()