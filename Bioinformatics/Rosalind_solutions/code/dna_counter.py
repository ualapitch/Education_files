import argparse
from collections import Counter
import os


def dna_counter(name):
    if os.path.isfile(name):
        with open(name, 'r') as f:
            dna = f.read().upper()
            dna_counts = Counter(dna)
            return f"{dna_counts['A']} {dna_counts['C']} {dna_counts['G']} {dna_counts['T']}"
    else:
        dna = name.upper()
        dna_counts = Counter(dna)
        if set(dna_counts.keys()).issubset({'A', 'G', 'C', 'T', r'\n'}):
            return f"{dna_counts['A']} {dna_counts['C']} {dna_counts['G']} {dna_counts['T']}"
        else:
            return f"You did something wrong!"


psr = argparse.ArgumentParser(prog='Dna counter', description='Counts nucleotides in txt file or from input string ')
psr.add_argument('file_or_str', help="path have to be enclosed in ''")
args = psr.parse_args()
print(dna_counter(args.file_or_str))
