import argparse
import os
import useful_func


def replace_u(string):
    cn = 0
    for n in string:
        if n == 'T':
            string[cn] = 'U'
        cn += 1


def rna_translator(name) -> str:
    if not os.path.isfile(name):
        dna = list(name.upper())
        if set(dna).issubset({'A', 'G', 'C', 'T', '\n'}):
            replace_u(dna)
            return f"{''.join(dna)}"
        else:
            return f"You did something wrong!"
    else:
        with open(name, 'r') as f:
            dna = list(f.read().upper())

            if set(dna).issubset({'A', 'G', 'C', 'T', '\n'}):
                replace_u(dna)
                return f"{''.join(dna)}"
            else:
                return f"You did something wrong!"


psr = argparse.ArgumentParser(prog='RNA transtalor',
                              description='Translate DNA in RNA from txt file or from input string')
psr.add_argument('-pors', help='path have to be enclosed in \'\'')
args = psr.parse_args()
res = rna_translator(input('Text path or str that you want to tranlate to RNA:\n'))
print(res)
print(useful_func.result_file(rna_translator, res))
