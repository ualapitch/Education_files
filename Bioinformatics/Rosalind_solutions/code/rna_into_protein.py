import pandas as pd
import numpy as np
import functools
import time


def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.4f} secs")
        return result
    return _wrapper


@timer
def rna_into_protein_1(sequence):
    splited_sequence = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    protein = ''
    for codon in splited_sequence:
        for col in codon_table.columns:
            if col == 'stop':
                break
            for value in codon_table.loc[:, col]:
                if value == codon:
                    protein += col

    return protein


@timer
def rna_into_protein_2(sequence):
    splited_sequence = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    protein = ''
    for codon in splited_sequence:
        amino_acid = codons.loc[codon[0], (codon[1], codon[2])]
        if amino_acid == 'stop':
            break
        else:
            protein += amino_acid
    return protein


codon_dct = {'A': ['GCU', 'GCC', 'GCA', 'GCG'],
             'C': ['UGU', 'UGC'],
             'D': ['GAU', 'GAC'],
             'E': ['GAA', 'GAG'],
             'F': ['UUU', 'UUC'],
             'G': ['GGA', 'GGC', 'GGG', 'GGU'],
             'H': ['CAU', 'CAC'],
             'I': ['AUU', 'AUC', 'AUA'],
             'K': ['AAA', 'AAG'],
             'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
             'M': ['AUG'],
             'N': ['AAU', 'AAC'],
             'P': ['CCU', 'CCC', 'CCA', 'CCG'],
             'Q': ['CAA', 'CAG'],
             'R': ['AGA', 'AGG', 'CGA', 'CGC', 'CGG', 'CGU'],
             'S': ['AGC', 'AGU', 'UCU', 'UCC', 'UCA', 'UCG'],
             'T': ['ACU', 'ACC', 'ACA', 'ACG'],
             'V': ['GUU', 'GUC', 'GUA', 'GUG'],
             'W': ['UGG'],
             'Y': ['UAU', 'UAC'],
             'stop': ['UAA', 'UAG', 'UGA']}


codon_table = pd.DataFrame({aa: pd.Series(codon_dct[aa], index=range(len(codon_dct[aa]))) for aa in codon_dct})
bases = ['A', 'U', 'C', 'G']
mi = [[base for base in bases for k in range(4)], bases*4]
codons = pd.DataFrame(index=bases, columns=pd.MultiIndex.from_arrays(mi))
for row in codons.index:
    for col in codons.columns:
        codon = row + ''.join(list(col))
        for col1 in codon_table.columns:
            for codon1 in codon_table.loc[:, col1]:
                if codon1 == codon:
                    codons.loc[row, col] = col1

with open(r'D:\Education_files\Bioinformatics\Rosalind_solutions\data\input_data\rosalind_prot.txt', 'r') as f:
    seq = f.read()
    res1 = rna_into_protein_1(seq)
    res2 = rna_into_protein_2(seq)
    with open('../data/output_data/res.txt', 'w') as file:
        print(res2, file=file)
