from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band,Musician,Guitarist,Bassist,Drummer
import pytest

def test_guitarist_str(): 
    actual=str(Guitarist("Ali"))
    expected="I am  : Ali , Plays : "
    assert actual==expected

def test_guitarist_repr(): 
    actual=repr(Guitarist("Ali"))
    expected="I am  : Ali , Plays : "
    assert actual==expected

# @pytest.fixture
# def prep():
#     Guitarist()
#     Bassist() 
#     Drummer()   

def test_version():
    assert __version__ == '0.1.0'
