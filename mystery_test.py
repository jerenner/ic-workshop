# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pytest import mark
from hypothesis import given, example
from hypothesis.strategies import integers

import mystery as mys

@given(integers(), integers())
@example(3, 0)
def test_2(a, b):
    assert mys.xxx(a, b) == mys.xxx(b, a)

@given(integers(), integers(), integers())
@example(3, 0, 1)
def test_3(a, b, c):
    assert mys.xxx(a, mys.xxx(b, c)) == mys.xxx(mys.xxx(a, b), c)
    