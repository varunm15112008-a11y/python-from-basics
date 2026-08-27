# Ask for the user's name
name = input("Enter your name: ")

# Ask for the user's age and convert it to a number
age = int(input("Enter your age: "))

# Print a customized greeting
print(f"Hello, {name}!")

# Check if the user is an adult
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
