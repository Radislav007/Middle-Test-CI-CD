import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))  # Замість 'src' використайте директорію, де знаходиться main.py

import pytest
from main import get_top_words

@pytest.fixture
def sample_text_file(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("Python is great. Python is dynamic. Python is easy.")
    return file

@pytest.mark.parametrize("top_n, expected_word", [(1, "python"), (2, "is")])
def test_get_top_words(sample_text_file, tmp_path, top_n, expected_word):
    output_file = tmp_path / "output.txt"
    get_top_words(sample_text_file, output_file, top_n=top_n)
    with open(output_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        assert expected_word in lines[0]
