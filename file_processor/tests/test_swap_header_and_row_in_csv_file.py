import os
import sys
import tempfile

from hw.file_processor import swap_header_and_row_in_csv_file

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))


def test_swap_header_and_row_in_csv_file():
    header = ['Name', 'Age']
    row = ['Alice', '30', 'Extra']

    swap_header_and_row_in_csv_file(header, row)

    with open('swapped_file.csv') as f:
        lines = [line.strip() for line in f.readlines()]

    assert lines[0] == 'Alice,30,Extra'  # row became header
    assert lines[1] == 'Name,Age,'       # header became row and padded

    os.remove('swapped_file.csv')
