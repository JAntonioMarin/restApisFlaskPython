friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anner"}

both = art.intersection(science)
print(both)

all_students = art.union(science)
print(all_students)