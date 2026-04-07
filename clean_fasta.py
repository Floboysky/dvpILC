#!/usr/bin/env python3

"""
Script that removes the /*** comments from a .fasta or .paml alignment file for EasyCodeML
"""

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as fin, open(output_file, "w") as fout:
    for line in fin:
        line = line.rstrip("\n")
        if "/" in line:
            line = line.split("/", 1)[0]  # Keep only the characters before the first "/"
        fout.write(line + "\n")

print(f"File written to: {output_file}")
