# test_vowels.py
import pytest
from vowels import count_vowels

def test_vowels_only():
    assert count_vowels('aeiou') == 5


def test_no_vowels():
    assert count_vowels('bcdfg') == 0


def test_mixed_string():
    assert count_vowels('HelloWorld') == 3


def test_vowels_only_cyrillic():
    assert count_vowels('аеёиоуыэюя') == 10


def test_no_vowels_cyrillic():
    assert count_vowels('бвгджзклмнпрстфхцчшщъь') == 0


def test_mixed_string_cyrillic():
    assert count_vowels('Привет Мир') == 3