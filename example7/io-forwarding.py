#!/usr/bin/env python

import argparse
import time

parser = argparse.ArgumentParser(description="forward I/O requests for seconds")
parser.add_argument(
    "integer",
    metavar="S",
    type=int,
    help="an integer for the number of seconds to compute",
)

args = parser.parse_args()

print("Will forward I/O requests for " + str(args.integer) + " seconds.")
time.sleep(args.integer)
