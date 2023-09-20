# set path
import sys
import path 
import pytest

directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

import file 
def test_add():
    expected = 5
    result = file.add(2, 3)
    assert expected == result

def test_substraction():
    expected = 4
    result = file.substraction(10, 6)
    assert expected == result

def test_hello():
    expected = 'say Hi'
    result = file.hello('Hi')
    assert expected == result
