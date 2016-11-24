#!/usr/bin/env python

import re
import os
import sys
import numpy

def main():
  lines = sys.stdin.read().split('\n')

  float_re = re.compile(r'([0-9]+)\.([0-9]+)')
  all_regular_floats = True

  min_digits = -1;

  values = []
  for line in lines:
    if line.strip()=='':
      continue

    match = float_re.match(line)
    all_regular_floats = all_regular_floats and match

    if match:
      ndigits = len(match.group(2))

      if min_digits == -1 or ndigits < min_digits:
        min_digits = ndigits

    values.append(float(line))


  arr = numpy.array(values)

  format = '%f +- %f'
  if all_regular_floats:
    format = '%%.%df +- %%.%df' % (ndigits, ndigits)

  print format % ( arr.mean(), arr.std() )

if __name__ == '__main__':
  main()
