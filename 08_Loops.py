# while loop
i = 0
while i < 3:
    print("meow")
    i = i + 1


# for loop
for i in range(3): # using the range function to loop n times
    print("meow")



print("meow\n" * 3, end="") # using string multiplication to print n times



while True:
    n = int(input("How many times? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("How many times? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")
