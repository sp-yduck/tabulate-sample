import os
from tabulate import tabulate


if __name__ == "__main__":

    rows = ["a", "b", "c"]    
    data = {
        "A": ['o', 'o', 'o'],
        "B": ['o', 'o', 'x'],
        "C": ['o', 'x', 'x'],
    }

    table = tabulate(data, headers='keys', showindex=rows, tablefmt='github')
    print(table)

    file_dir = "example/"
    file_name = "README.md"
    file_path = os.path.join(file_dir, file_name)
    os.makedirs(file_dir, exist_ok=True)

    with open(file_path, mode='w') as f:
        f.write(table)