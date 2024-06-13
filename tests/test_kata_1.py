import pytest

from katas.kata_1 import *

def test_bracket_matcher() -> None:
    assert bracket_matcher("()") == True
    assert bracket_matcher("([]{})") == True
    assert bracket_matcher("([)]") == False
    assert bracket_matcher("((()))") == True
    assert bracket_matcher("{{[[(())]]}}") == True
    assert bracket_matcher("{{[[())]]}}") == False

    