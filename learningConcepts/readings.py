import sys
import numpy


def main():
    script = sys.argv[0]
    filenames = sys.argv[1:]
    assert len(filenames)>0, script+" takes one or more input arguments."
    for filename in filenames:
        print(filename+":")
        data = numpy.loadtxt(filename, delimiter=",")
        for line in data:
            print(line)
        for m in numpy.mean(data, axis=1):
            print(m)
        print("-------------------------------------\n")

if __name__ == "__main__":
    main()
