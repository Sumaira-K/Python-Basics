def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    if n % 2 == 0:    # return (n % 2 == 0) would also work
        return True
    else:
        return False

main()
