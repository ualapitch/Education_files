from usefull_funcs import save_func_return_to_file


@save_func_return_to_file
def dna_substring_1(substring, main_string):
    res_ls = []
    i = 0
    l = len(substring)
    while i != len(main_string) - l:
        if main_string[i:i+l] == substring:
            res_ls.append(i+1)
        i += 1
    return res_ls


with open(r'D:\Education_files\Bioinformatics\Rosalind_solutions\data\input_data\rosalind_subs (2).txt', 'r') as f:
    strings = f.read().split('\n')
    main_str = strings[0]
    sub_str = strings[1]
    print(*dna_substring_1(sub_str, main_str), sep=' ')
