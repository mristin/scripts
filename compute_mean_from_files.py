#!/usr/bin/env python

import os, sys, re, math

def main():
  values = []
  for path in sys.argv[1:]:
    f = open(path, 'rt')
    value_str = f.read()
    f.close()

    try:
      value = float(value_str)
    except ValueError:
      print("Value '%s' is not a float." % (value_str))
      return 1

    values.append(value)

  mean = sum(values) / len(values)
  print "%.6f" % mean

if __name__ == '__main__':
  main()
