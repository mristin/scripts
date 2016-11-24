#!/usr/bin/env python

from plumbum import local
import sys

def main():
  try:
    if len(sys.argv) != 2:
      print "usage: git-current-branch.py [path to directory]"
      sys.exit(1)

    path = sys.argv[1]
    local.cwd.chdir(path)
    current_branch = local["git"]["rev-parse"]["--abbrev-ref"]["HEAD"]().strip()
    print current_branch
  except:
    pass

if __name__ == "__main__":
    main()
