def hello():
    print("Hello!")

hello()

def user_age_in_seconds():
    user_age = int (input("Enter you age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")


print("Welcome to the age in seconds program!")
user_age_in_seconds()

print("Goodbye!")

friends = ["Rolf", "Bob"]

# Cant do
# def add_friends(friends):
#     friend_name = input("Enter your friend name: ")
#     friends = friends + [friend_name]

def add_friend():
    friends.append("Paco")

add_friend()

print(friends)

