import pytest
from string_reversal import reverse_string


def test_basic_reversal():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"


def test_empty_string():
    assert reverse_string("") == ""


def test_palindrome():
    s = "madam"
    assert reverse_string(s) == s


def test_whitespace_and_symbols():
    assert reverse_string("  abc ") == " cba  "
    assert reverse_string("123!@#") == "#@!321"


def test_unicode_characters():
    assert reverse_string("äöü") == "üöä"
    assert reverse_string("你好") == "好你"


def test_non_string_input():
    with pytest.raises(TypeError):
        reverse_string(123)
    with pytest.raises(TypeError):
        reverse_string(None)
