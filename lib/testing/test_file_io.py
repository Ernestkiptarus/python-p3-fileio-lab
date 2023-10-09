# tests/test_file_io.py
from lib.file_io import write_file, append_to_file, read_file

def test_write_file_and_read_file():
    write_file(file_name="testfile", file_content="Test Content")
    content = read_file(file_name="testfile")
    assert content == "Test Content"

def test_append_to_file():
    append_to_file(file_name="testfile", append_content="Additional Content")
    content = read_file(file_name="testfile")
    assert content == "Test Content\nAdditional Content\n"
