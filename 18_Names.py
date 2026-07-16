names = []
for _ in range(3):
    name = input("What's your name? ")
    names.append(name)

for name in sorted(names):
    print(f"Hello, {name}")


# using files
#writing to a file
name = input("What's your name? ")
with open("names.txt", "a") as file:  #file.open()
    file.write(f"{name}\n")
#file.close() 


#reading from a file
with open("names.txt", "r") as file:
    for line in sorted(file):
        print("hello, " , line.rstrip())


"""   lines = file.readlines()

for line in lines:
    print("hello, ", line.rstrip()) """ 


#sorted names
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse = True):
    print(f"hello, {name}")
