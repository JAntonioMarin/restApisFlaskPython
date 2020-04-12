a = []
b = a

a.append(35)

print(id(a))
print(id(b))

print(a)
print(b)

a = []
b = []

print(id(a))
print(id(b))

a = 8597
b = 8597

print(id(a))
print(id(b))

a = 8598

print(id(a))
print(id(b))