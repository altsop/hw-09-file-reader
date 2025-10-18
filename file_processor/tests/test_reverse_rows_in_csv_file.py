import os
import sys
import tempfile

from hw.file_processor import reverse_rows_in_csv_file

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))


def test_reverse_rows_in_csv_file():
    with tempfile.NamedTemporaryFile('w+', delete=False) as tmp_in:
        tmp_in.write("a,b,c\n1,2,3\nx,y,z\n")
        input_path = tmp_in.name

    tmp_out = tempfile.mktemp()

    try:
        reverse_rows_in_csv_file(input_path, tmp_out)
        with open(tmp_out) as f:
            lines = f.readlines()
        assert lines == ['x,y,z\n', '1,2,3\n', 'a,b,c\n']
    finally:
        os.remove(input_path)
        if os.path.exists(tmp_out):
            os.remove(tmp_out)
