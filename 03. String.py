name = input("What is your name? ").strip().title()

# Remove any leading/trailing whitespace and capitalize the first letter of the name
name = name.strip().title()  

#Spliting name into first and last name
first_name, last_name = name.split(" ", 1)  # Split the name into first and last name
print(f"Hello, {first_name}!")

#It will not remove spaces in between the first and last name only the leading and trailing spaces. It will also capitalize the first letter of each word in the name.
