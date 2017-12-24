import sys
import numpy
import glob

def function():
    data = numpy.loadtxt("inflammation-01.csv",delimiter=",")
    print(data)

if __name__ == "__main__":
    function()
else:
    print("test.py is being imported.")
