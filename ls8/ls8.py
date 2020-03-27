#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

print(f"sys.argv: {sys.argv}")

if len(sys.argv) != 2: 
    print(f"usage: file.py filename")

filename = sys.argv[1]
program = []

with open(filename) as f:
    for line in f:
        # ignore comments
        comment_split = line.split("#")
        #print(comment_split)
        # strip out whitespace
        num = comment_split[0].strip()
        if num:
            num = int(num, 2)
            
            #print(num)
            program.append(num)
            
print(f"\nprogram to run: {program}\n")

cpu = CPU()

cpu.load(program)
cpu.run()