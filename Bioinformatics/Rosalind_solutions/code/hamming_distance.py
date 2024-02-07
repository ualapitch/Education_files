from usefull_funcs import save_func_return_to_file


def hamming_distance(seq1, seq2):
    dist = 0
    for base1, base2 in zip(seq1, seq2):
        if base1 != base2:
            dist += 1

    return dist


with open(r'D:\Education_files\Bioinformatics\Rosalind_solutions\data\input_data\rosalind_hamm.txt', 'r') as f:
    inp = f.read().split('\n')
    print(hamming_distance(inp[0], inp[1]))
