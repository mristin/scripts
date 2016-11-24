#!/usr/bin/env python

import sys
import re

def main():
  orig_lines = []
  for line in sys.stdin.readlines():
    sys.stdout.write(line)
    orig_lines.append(line)

  sys.stdout.write('\n')

  empty_re = re.compile(r'^[ ]*$')
  keyword_re = re.compile(r'^[ ]*(public:|protected:|private:|};)[ ]*$')
  class_re = re.compile(
    r'^[ ]*class[ ]+([A-Za-z0-9_]+)')

  indent_re = re.compile(r'^[ ]*(.*)$')

  empty_imp_re = re.compile(r'.*{[ ]*}[ ]*[;]*$')

  classname = None

  code_lines = []
  for line in orig_lines:
    if empty_re.match(line) or keyword_re.match(line):
      continue;

    class_match = class_re.match(line)
    if class_match:
      classname = class_match.group(1)
      continue;

    if empty_imp_re.match(line):
      continue

    indent_match = indent_re.match(line)
    code_lines.append(indent_match.group(1))

  code = ''.join(code_lines)
  code_lines = code.split(';')

  pure_virtual_method_re = re.compile(r'^.*[ ]*=[ ]*0[ ]*$')
  virtual_method_re = re.compile(
        r'virtual[ ]+([a-zA-Z_0-9<>: ]+[^ ])[ ]+([A-Z_a-z0-9]+)[ ]*([^ ].*)$')

  method_re = re.compile(
            r'([a-zA-Z_0-9<>: ]+[^ ])[ ]+([A-Z_a-z0-9]+)[ ]*([^ ].*)$')

  constructor_re = re.compile('^%s(.*)$' % classname)
  deconstructor_re = re.compile('^~%s(.*)$' % classname)

  stubs = []
  for stmt in code_lines:

    if '(' not in stmt:
      continue

    if pure_virtual_method_re.match(stmt):
      continue

    constructor_match = constructor_re.match(stmt)
    if constructor_match:
      stubs.append('%s::%s%s {\n}' % (classname,
                                 classname,
                                 constructor_match.group(1)))
      continue;

    deconstructor_match = deconstructor_re.match(stmt)
    if deconstructor_match:
      stubs.append('%s::~%s%s {\n}' % (classname,
                                 classname,
                                 deconstructor_match.group(1)))
      continue;


    method_match = virtual_method_re.match(stmt)

    if not method_match:
      method_match = method_re.match(stmt)

    if method_match:
      stubs.append('%s %s::%s%s {\n}' % (method_match.group(1),
                                       classname,
                                       method_match.group(2),
                                       method_match.group(3)))



  result = '\n\n'.join(stubs)
  sys.stdout.write(result)

if __name__ == '__main__':
  main()
