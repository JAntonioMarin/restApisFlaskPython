def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25)

def named2(name, age):
    print(name, age)


details = {"name": "Bob", "age": 25}

named2(**details)

named(**details)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age = 25)

def myfunction(**kwargs):
    print(kwargs)

# myfunction(**"Bob") # Error, must be a mapping
# myfunction(**None)