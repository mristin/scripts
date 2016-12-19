#!/usr/bin/env python3

import os, sys, re,subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    answer = input(bcolors.OKBLUE + "Name of the new branch (spaces will be replaced with '-'): " + bcolors.ENDC)

    answer=answer.replace(' ', '-')
    subprocess.check_call(['git', 'checkout', '-b', answer])

if __name__ == "__main__":
    main()
