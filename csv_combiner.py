from pathlib import Path
import argparse


def process(line, filename):
    """

    :param line:
    :param filename:
    :return:
    """
    columns = line.split(",")
    columns = [column.strip() for column in columns]
    columns.append(filename)
    return ", ".join(columns)


def get_headers(filepath):
    """
    :param filepath:
    :return:
    """
    try:
        with open(filepath) as f:
            return process(f.readline(), "filename")
    except FileNotFoundError:
        print(f"File does not exist: {filepath}")
        return False


def scan_files(filepaths):
    """
    :param filepaths:
    :return: None
    """
    headers = get_headers(filepaths[0])
    print(headers)
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