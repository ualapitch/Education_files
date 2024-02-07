def save_func_return_to_file(func):
    def _wrapper(*args, **kwargs):
        func_return = func(*args, **kwargs)
        with open(fr'D:\Education_files\Bioinformatics\Rosalind_solutions\data\output_data\{func.__name__}_return.txt',
                  'w') as f:
            print(func_return, file=f)
        return func_return
    return _wrapper