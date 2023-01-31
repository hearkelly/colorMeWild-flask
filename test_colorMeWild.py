import pytest
from alphabet import Alphabet

def test_pass():
    assert True
def test_fail():
    assert False

ABC = Alphabet()
def test_Alphabet():
    assert isinstance(ABC,Alphabet)

def test_attributes():
    assert hasattr(ABC, "id")
    assert hasattr(ABC, "colorDict")
    assert hasattr(ABC, "histDict")
    assert hasattr(ABC, "avgColor")

def test_id():
    assert type(ABC.id) == str

def test_colorDict():
    assert len(ABC.colorDict) == 256

