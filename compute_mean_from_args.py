#!/usr/bin/env python

import os, sys, re,math

def main():
  if len(sys.argv) < 2:
    print "Usage: compute_mean_from_args.py [set of numbers]"
    sys.exit(1)

  values = []
  for value_str in sys.argv[1:]:
    try:
      value = float(value_str)
    except ValueError:
      print("Value '%s' is not a float." % (value_str))
      exit(1)

    values.append(value)

  mean = sum(values) / len(values)

  print "%.6f" % mean


if __name__ == '__main__':
  main()
