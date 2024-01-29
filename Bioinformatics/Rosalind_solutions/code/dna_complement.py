import os
from useful_func import result_file


def dna_comp(dna) -> None:
    cn = 0
    for n in dna:
        for cern, repn in [('A', 'T'), ('T', 'A'), ('G', 'C'), ('C', 'G')]:
            if cern == n:
                dna[cn] = repn
        cn += 1


def dna_complement(name) -> str:
    if not os.path.isfile(name):
        dna = list(name.upper())
        if set(dna).issubset({'A', 'G', 'C', 'T', '\n'}):
            dna_comp(dna)
            return f"{''.join(dna[::-1])}"
        else:
            return f"You did something wrong!"
    else:
        with open(name, 'r') as f:
            dna = list(f.read().upper())
            if set(dna).issubset({'A', 'G', 'C', 'T', '\n'}):
                dna_comp(dna)
                return f"{''.join(dna[::-1])}"
            else:
                return f"You did something wrong!"


nam = input('Text path or str with DNA you want to make reverse complement molecule:\n')
print(dna_complement(nam))
result_file(dna_complement, nam)
