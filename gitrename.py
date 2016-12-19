#!/usr/bin/env python3

import os
import sys
import re
import subprocess

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    IN = '\033[93m'
    ENDC = '\033[0m'

def main():
  if len(sys.argv) is 1:
    new_branch = input(bcolors.OKBLUE + "Name of the new branch (spaces will be replaced with '-'): " + bcolors.ENDC)
  elif len(sys.argv) is 2:
    new_branch = sys.argv[1]
  else:
    print("Usage: {} [new branch name]".format(os.path.basename(__file__)))
    sys.exit(1)

  current_branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()

  chosen = ""

  while True:
    print()
    print("Renaming the branch " + bcolors.OKGREEN + current_branch + bcolors.ENDC + \
        " to " + bcolors.OKGREEN + new_branch + bcolors.ENDC + "?")
    answer = input("[yN] > ")

    if answer.startswith("n") or answer.startswith("N"):
      sys.exit(1)
    elif answer == "y" or answer == "Y" or answer == "yes" or answer == "Yes":
      subprocess.check_call(['git', 'branch', '-m', current_branch, new_branch])
      subprocess.check_call(['git', 'push', 'origin', ':' + current_branch])
      subprocess.check_call(['git', 'push', '--set-upstream', 'origin', new_branch])

      sys.exit(0)

    elif answer == "q" or answer == "":
      sys.exit(1)
    else:
      print("Answer " + bcolors.IN + answer + bcolors.ENDC + " has not been recognized.")

  print()


if __name__ == "__main__":
  main()
