"""Tests for binaryConvertor.py"""

import pytest
import binaryConvertor


def test_binaryConvertor():
    """Testing if it converts correctly"""
    assert binaryConvertor.convert(0) == "0"
    assert binaryConvertor.convert(10) == "1010"
    assert binaryConvertor.convert(50) == "110010"
    assert binaryConvertor.convert(100) == "1100100"


def test_bounds():
    """Testing proper bounds"""
    with pytest.raises(ValueError):
        binaryConvertor.convert(-1)
    with pytest.raises(ValueError):
        binaryConvertor.convert(101)


def test_float():
    """Testing if it doesn't convert floats"""
    with pytest.raises(ValueError):
        binaryConvertor.convert(20.12)
