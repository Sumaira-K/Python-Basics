# PyPi website for packages: https://pypi.org/
#pip is used to install packages from PyPi

#cowsay package
import cowsay
import sys
if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])