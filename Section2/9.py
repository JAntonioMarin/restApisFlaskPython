name = "Bob"
greeting = "Hello, Bob"

print(greeting)

name = "Rolf"
greeting = f"Hello, {name}"

print(greeting)

name = "Rolf"
greeting = "Hello, {} {}"

with_name = greeting.format(name, "Jejeje")

print(with_name)