import os


def delete_no_seq(path) -> None:
    """Delete all no letters"""
    with open(path, 'r') as f:
        dna = list(f.read().upper())
        cn = 0
        name = os.path.basename(path)
        name_slice = name[:name.find('.')]
        for ch in dna:
            if ch.isalpha():
                pass
            else:
                dna[cn] = ''
            cn += 1
        with open(f'{name_slice}_afr_pcg.txt', 'w') as file:
            file.write(''.join(dna))


def result_file(function, name) -> None:
    """Make a file with func result"""
    with open(f'result_{function.__name__}.txt', 'w') as f:
        f.write(function(name))
        print(f'Have been made file with result named result_{function.__name__}.txt')


def create_bat() -> None:
    """Make a batch file from .py script"""
    path_to_script = input('Text path to script with:\n')
    with open(fr'{os.path.basename(path_to_script)[:-3]}.bat', 'w') as f:
        f.writelines(['@echo off\n', f'"C:\\Users\\Vasiliy\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" '
                                     f'"{path_to_script}"\n', 'pause'])

