from hypothesis import given 
from hypothesis.strategies import text

@given(text())
def test_sample(s: str):
    assert True

