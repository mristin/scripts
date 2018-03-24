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
    
    subprocess.check_output(['git', 'commit', '-m', msg])
    

if __name__ == "__main__":
    main()
