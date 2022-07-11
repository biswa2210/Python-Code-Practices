
txt = "Hello, welcome to my world."

x = txt.find("welcome")
y = txt.find("e")
z = txt.find("e", 5, 10)

p = txt.rfind("welcome")
q = txt.rfind("e")
r = txt.rfind("e", 5, 10)

print(x)
print(y)
print(z)
print(p)
print(q)
print(r)