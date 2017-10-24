#!/usr/bin/python2

# sypy.py: Example interpreter for Symbolic Python.
# Call with command line arguments: <script-file> [input]


import sys
import ast

script = open(sys.argv[1]).read()

if len(sys.argv) > 2:
  _ = ast.literal_eval(sys.argv[2])
else:
  _ = None

for char in script:
  if char.isalnum():
    print("Invalid script: the %r character is banned." % char)
    quit()

def __(cmd):
  for i,j in globals().items(): locals()[i] = j
  exec cmd
  del cmd
  for i,j in locals().items(): globals()[i] = j

exec script

print _
