x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

if x>y:
    print(f"{x} is greater than {y}")
elif x>=y:
    print(f"{x} is greater than or equal to {y}")
elif x<y:
    print(f"{x} is less than {y}")
elif x<=y:
    print(f"{x} is less than or equal to {y}")
elif x!=y:
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")
if x>y or x<y:
    print(f"{x} is not equal to {y}")
if x>y and x!=y:
    print(f"{x} is greater than {y} and not equal to {y}")
