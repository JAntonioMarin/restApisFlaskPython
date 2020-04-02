# List
l = ["Bob", "Rolf","Anne"]
# Tuple
t = ("Bob", "Rolf","Anne")
# Set
s = {"Bob", "Rolf","Anne"}

print(l[0])
print(t[0])
# print(s[0])

l[0] = "Pepe"
# t[0] = "Pepe"
l.append("Pepito")
l.remove("Pepe")
print(l)

s.add("Smith")
s.add("Smith")
print(s)