def main():
    x = get_int()
    print(f"The number you entered is: {x}")
def get_int():
    while True:
        try:
            x = int(input("Enter a number: "))
            return x
        except ValueError:
           pass  # Ignore the error and prompt again
main()

# SyntaxError: invalid syntax
# RuntimeError
# ValueError: invalid literal for int() with base 10: 'abc'
# NameError: name 'x' is not defined
# pass statement