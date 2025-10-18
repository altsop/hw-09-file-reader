import sys
import os
import csv

from file_processor.file_processor import mesh_two_list_to_csv_file

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))


def test_mesh_two_list_to_csv_file():
    list1 = ['A1', 'A2', 'A3']
    list2 = ['B1', 'B2', 'B3']
    filename = 'test_output.csv'

    mesh_two_list_to_csv_file(list1, list2, filename)

    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row, expected in zip(reader, zip(list1, list2)):
            assert row == list(expected), f"Row {row} does not match expected {expected}"

    os.remove(filename)

