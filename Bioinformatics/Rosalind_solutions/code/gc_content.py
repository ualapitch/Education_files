with open(r'D:\Education_files\Bioinformatics\Rosalind_solutions\data\input_data\rosalind_gc.txt', 'r') as f:
    data = f.read()
    data_splited = [seq.split('\n') for seq in data.split('>')][1:]
    res_ls = []
    for part in data_splited:
        num_empty = part.count('')
        for i in range(num_empty):
            part.remove('')
        seq = ''.join(part[1:])
        res_ls.append((part[0], seq, (seq.count('G') + seq.count('C'))/len(seq)*100))
    res_ls.sort(key=lambda x: x[2], reverse=True)
    print(res_ls[0][0],'\n', res_ls[0][2])


