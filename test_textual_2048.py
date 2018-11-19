
from game2048.textual_2048 import *
from pytest import *

def mock_read(obj):
    return "0"

def test_read_player_command(monkeypatch):
    monkeypatch.setattr('builtins.input', mock_read)
    a= read_player_command()
    assert a == "0"

def test_inputs(monkeypatch):
    monkeypatch.setattr('builtins.input', mock_read)
    assert type(read_size_grid()) == int
    assert type(read_player_command()) == str



