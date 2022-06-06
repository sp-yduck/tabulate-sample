import os
from tabulate import tabulate


def readmate(title:str, table:str, file_dir:str, file_name:str):
    file_path = os.path.join(file_dir, file_name)
    os.makedirs(file_dir, exist_ok=True)

    content = f"# {title}\n\n" + table

    with open(file_path, mode='w') as f:
        f.write(content)


if __name__ == "__main__":

    rows = ["a", "b", "c"]
    data = {
        "A": ['o', 'o', 'o'],
        "B": ['o', 'o', 'x'],
        "C": ['o', 'x', 'x'],
    }
    table = tabulate(data, headers='keys', showindex=rows, tablefmt='github')

    file_dir = "example/"
    file_name = "README.md"
    title = "This is a example file"
    readmate(title=title, table=table, file_dir=file_dir, file_name=file_name)