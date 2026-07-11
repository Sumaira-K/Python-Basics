import statistics
print(statistics.mean([100, 90]))

# Command line arguements: used to pass information to a program when it is run from the command line.
import sys
if len(sys.argv) < 2:
    sys.exit("too few arguments")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")
else:
    print("hello, my name is", sys.argv[1])