#! /usr/bin/env python3

import re
from sys import argv

def getSum(filename):
    return sum([int(num) for num in re.findall("[0-9]+", open(filename).read())])

if __name__ == "__main__":
    if len(argv) < 2:
        print("usage: extract_sum filename")
        quit(1)
    else:
        print(getSum(argv[1]))
