import sys
import numpy

def main():
    script = sys.argv[0]
    assert len(sys.argv)>1, script+" takes one or more input arguments: '"+script+" [--max, --min, --mean] filename'"
    action = sys.argv[1]
    assert action in ['--max','--min', '--mean'], \
        action+" is not one of the allowed actions: [--max, --min, --mean]"

    filenames = sys.argv[2:]
    if len(filenames) == 0:
        process(sys.stdin, action)
    else:
        for filename in filenames:
            process(filename, action)


def process(filename, action):
    data = numpy.loadtxt(filename, delimiter=",")
    values = []
    if action == "--max":
        values = numpy.max(data,axis=1)
    elif action == "--min":
        values = numpy.min(data,axis=1)
    elif action == "--mean":
        values = numpy.mean(data,axis=1)
    for value in values:
        print(value)
    print("-----------------")
if __name__ == "__main__":
    main()
