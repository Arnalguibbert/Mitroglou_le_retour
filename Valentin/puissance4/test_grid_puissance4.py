# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:58:04 2018

@author: Valentin
"""

from pytest import *
from grid_puissance4 import *

def test_init_grid():
    game_grid = init_grid(7)
    assert game_grid == [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

def test_update_grid():
    game_grid = update_grid(init_grid(7),3,"0")
    game_grid = update_grid(game_grid,3,"1")
    game_grid = update_grid(game_grid,2,"0")
    assert game_grid == [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', '1', ' ', ' ', ' '],
    [' ', ' ', '0', '0', ' ', ' ', ' ']]

def test_move_possible():
    assert  move_possible(init_grid(7),"2") == True
    game_grid = update_grid(init_grid(7),0,"0")
    game_grid = update_grid(game_grid,0,"1")
    game_grid = update_grid(game_grid,0,"0")
    game_grid = update_grid(game_grid,0,"1")
    game_grid = update_grid(game_grid,0,"0")
    game_grid = update_grid(game_grid,0,"1")
    game_grid = update_grid(game_grid,0,"0")
    assert move_possible(game_grid,"0") == False













