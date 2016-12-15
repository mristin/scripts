#!/usr/bin/env python3

import os, sys, re, subprocess

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    IN = '\033[93m'
    ENDC = '\033[0m'

def main():
    current_branch = subprocess.check_output(["git", "rev-parse", "-abbrev-ref", "HEAD"]).strip()

    lst = subprocess.check_output(["git", "show-branch", "--topo-order", "--no-color", "--list"]).split("\n")
    
    branchRe = re.compile(r'^[ *]*\[([^\]]*)\].*$')
    branches = list(reversed([branchRe.match(branch).group(1) for branch in lst if branch != ""]))

    for (branch_i, branch) in enumerate(branches):
        if branch == current_branch:
            print(bcolors.OKBLUE + ("%d) %s [CURRENT]" % (branch_i+1, branch)) + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + ("%d) %s" % (branch_i+1, branch)) + bcolors.ENDC)

    print
    print(bcolors.OKGREEN + "q) Quit" + bcolors.ENDC)
    print

    chosen = -1
    options = range(len(branches))

    while chosen not in options:
        answer = raw_input("Which branch to jump to? >")
        if answer.startswith("q"):
            sys.exit(1)

        try:
            chosen = int(answer) - 1
        except:
            pass

    print("Jumping to %s" % branches[chosen])
    subprocess.check_call(["git", "checkout", branches[chosen]])


if __name__ == "__main__":
    main()
