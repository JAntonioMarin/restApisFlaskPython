movies_watched = {"The Matrix", "Green Book", "Her"}

user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet")


number = 7
user_input = input("enter 'y' if you would like to play: ")

if user_input in ("y", "Y", "Yes", "yes"):
    user_number = int(input("Guess ourr number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("sorry, it's wrong!")



