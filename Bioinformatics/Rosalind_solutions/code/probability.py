def probability_dominant(dom_homo, hete, rec_homo):
    s = dom_homo + hete + rec_homo
    return dom_homo/s + hete/s*(0.5 + 0.5*(dom_homo/(s-1) + 0.5*(hete-1)/(s-1))) + rec_homo/s* (dom_homo/(s-1) + 0.5*hete/(s-1))


with open(r'D:\Education_files\Bioinformatics\Rosalind_solutions\data\input_data\rosalind_iprb.txt', 'r') as f:
    data = f.read().split(' ')
    print(probability_dominant(int(data[0]), int(data[1]), int(data[2])))