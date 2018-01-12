#!/usr/bin/env python3

import os, sys, re, subprocess, shlex

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    IN = '\033[93m'
    ENDC = '\033[0m'

def main():
    current_branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()
    print(current_branch)
    
    msg=current_branch.replace("mristin/", "").replace("-", " ")
    
    answer=''
    while answer not in ['y', 'n']:
       answer = input("git commit -m {}? Y/n >".format(shlex.quote(msg)))
    
    if answer == 'y' or answer == '':
        subprocess.check_output(['git', 'commit', '-m', msg])
    

if __name__ == "__main__":
    main()
