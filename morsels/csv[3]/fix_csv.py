import sys
import csv
import argparse

help_text = 'This is a test program. It demonstrates how to use the argparse module with a program description'

parser = argparse.ArgumentParser(description=help_text)
parser.add_argument("--in-delimiter=", "-d", help="set delimiter")
parser.add_argument("--in-quote=", "-q", help="set quote")
parser.add_argument("")
# --in-delimiter="|"
# --in-quote="'"
#cars.csv cars-fixed.csv

parser.parse_args()
