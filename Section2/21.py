numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

# for num in numbers:
#     doubled.append(num * 2)

print(doubled)

friends = ["Rolf", "Bob", "Jen", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]


# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(starts_s)


