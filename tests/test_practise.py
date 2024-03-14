import pytest

from katas.practise import *

def test_bracket_matcher() -> None:
    assert bracket_matcher("()") == True
    assert bracket_matcher("([]{})") == True
    assert bracket_matcher("([)]") == False
    assert bracket_matcher("((()))") == True
    assert bracket_matcher("{{[[(())]]}}") == True
    assert bracket_matcher("{{[[())]]}}") == False

    