for i in range(3):
    print('#')


# colums
def main():
    print_column(3)

def print_column(height):
    for i in range(height):  # print("#\n" * height, end="")
        print('#')

main()



# rows
def main():
    print_row(3)

def print_row(width):
    print('?' * width)

main()


# multiple rows and columns
def main():
    print_square(3)

def print_square(size):
    for i in range(size): #rows
        for j in range(size): #columns  # print("#" * size)
            print('#', end="")
        print()
main() 


# better version
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print('#' * width)

main()
