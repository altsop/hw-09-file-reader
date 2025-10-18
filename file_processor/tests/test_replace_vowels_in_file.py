import os
import sys
import tempfile

from file_processor.file_processor import replace_vowels_in_file

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))


def test_replace_vowels_in_file():
    # Create a temporary input file
    with tempfile.NamedTemporaryFile('w+', delete=False) as tmp_input:
        tmp_input.write("Hello World!\nAEIOU aeiou.")
        input_path = tmp_input.name

    # Temporary output file path
    tmp_output_path = tempfile.mktemp()

    try:
        replace_vowels_in_file(input_path, tmp_output_path)

        with open(tmp_output_path, 'r', encoding='utf-8') as f:
            result = f.read()

        expected = "H*ll* W*rld!\n***** *****."
        assert result == expected

    finally:
        os.remove(input_path)
        if os.path.exists(tmp_output_path):
            os.remove(tmp_output_path)