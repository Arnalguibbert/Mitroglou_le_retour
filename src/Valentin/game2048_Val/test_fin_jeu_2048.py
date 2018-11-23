# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 10:11:12 2018

@author: Valentin
"""

from fin_jeu_2048 import *
import pytest as pt


def test_is_grid_full():
    assert is_grid_full([[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]])


def test_move_possible():
    assert move_possible([[2, 2, 2, 2], [4, 8, 8, 16], [0, 8, 0, 4], [4, 8, 16, 32]]) == [True,True,True,True]
    assert move_possible([[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]]) == [False,False,False,False]


