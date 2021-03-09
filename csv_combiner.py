from pathlib import Path
import argparse
#import pytest


def process(line, filename):
    """
    This function takes a single line and process it to remove any white spaces and returns a string value

    :param line: A single row/line from the file
    :param filename: This argument contains the name of the file
    :return: a list string
    """
    columns = line.split(",")
    columns = [column.strip() for column in columns]
    columns.append(filename)
    return ", ".join(columns)


def get_headers(filepath):
    """
    This function is used to get the header records from each file

    :param filepath: The filepath input by the user
    :return: The header record for each file
    """

    try:
        with open(filepath) as f:
            return process(f.readline(), "filename")
    except FileNotFoundError:
        print(f"File does not exist: {filepath}")
        return False


def scan_files(filepaths):
    """
    :param filepaths: The filepaths input by the user
    :return: None
    """
    headers = get_headers(filepaths[0])
    for filepath in filepaths:
        p = Path(filepath)
        filename = p.name

        try:
            with open(filepath) as f:
                f.readline()
                for line in f:
                    # line = clean(line)
                    output_line = process(line, filename)
                    print(output_line)
        except FileNotFoundError:
            print(f"File does not exist: {filepath}")


def runner():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("filepaths", type=str, nargs="+")
    args = parser.parse_args()
    scan_files(args.filepaths)


if __name__ == "__main__":
    runner()