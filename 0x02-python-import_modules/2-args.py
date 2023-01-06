#!/usr/bin/python3
import sys
if __name__ == "__main__":
    # printing number of arguments
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("{} arguments.".format(num_args))
    elif num_args == 1:
        print("{} argument: ".format(num_args))
    else:
        print("{}: arguments:".format(num_args))

    # printing arguments
    for pos, args in enumerate(sys.argv[1:]):
        print("{}: {}".format(pos+1, args))
