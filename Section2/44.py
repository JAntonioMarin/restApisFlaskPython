def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


# grades = ["asd", 99,85, 100]
# grades = []
grades = [88, 99, 85, 100]

print("Welcome to the average grade program.")

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError:
    print("The are no grades yes in your list")
except TypeError:
    print("Error in value")
else:
    print(f"The average grade is {average}")
finally:
    print("Thank you!")
