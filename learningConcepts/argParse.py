import argparse

parser = argparse.ArgumentParser()
#parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("square", help="square the given number",type=int)

#adding optional arguments
parser.add_argument("--verbosity",help="change the verbosity of the output")

#adding a true or false only optional argument
parser.add_argument("--verbose",help="makes the output verbose", action="store_true")

#adding short version to optional arguments
parser.add_argument("-v", "--verb", help="adding some verbs", action="store_true")

args = parser.parse_args()

if args.verbosity:
    print("verbosity turned on")

if args.verbose:
    print("now everything is verbose")

if args.verb:
    print("adding likkle verbs")
print(pow(args.square,2))
