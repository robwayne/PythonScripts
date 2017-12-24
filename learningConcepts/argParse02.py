import argparse

parse = argparse.ArgumentParser()

#adding the arguments to the commandline
parse.add_argument("square",help="gives the square of the number",type=int)
parse.add_argument("-v","--verbose",help="makes the output of the script more verbose", action="store_true")
parse.add_argument("-t","--verbosity",help="changes the output to be show more information", type=int, choices=[0,1,2])

args = parse.parse_args()

answer = args.square**2

if(args.verbose or args.verbosity == 2):
    print("The square of {} equals {}.".format(args.square,answer))
elif (args.verbosity == 1):
    print("{}^2 = {}.".format(args.square,answer))
else:
    print(answer)
