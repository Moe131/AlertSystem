from pathlib import Path


def _read_input_file_path() -> Path:
    """Reads the input file path from the standard input"""
    return Path(input())

def readFileLines(path:Path, encoding = 'utf-8') -> list:
    """Reads the lines of a file with given path and returns them as a list"""
    with open(path, 'r', encoding = encoding) as the_file:
        return the_file.readlines()

def main() -> None:
    """Runs the simulation program in its entirety"""
    input_file_path = _read_input_file_path()
    inputLines = readFileLines(input_file_path)


if __name__ == '__main__':
    main()
