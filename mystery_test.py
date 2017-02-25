# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pytest import mark

import mystery as mys

@mark.parametrize( "a   b  c".split(),
                  ((1,  1, 2),
                   (1,  0, 1),
                   (1, -1, 0)))
def test_1(a, b, c):
    assert mys.xxx(a, b) == c

