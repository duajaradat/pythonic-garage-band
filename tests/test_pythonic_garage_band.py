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

def test_drummer_repr(): 
    actual=repr(Drummer("Ali"))
    expected="I am  : Ali , Plays : "
    assert actual==expected

def test_band_name(): 
    the_rock=Band("The Rock",[]) 
    assert the_rock.name=="The Rock"

def test_bassist_instrument(): 
    """
    test the bassist instance what instruments they play with
    """
    lele=Bassist("Cat") 
    assert lele.get_instrument()=="bass"  

# @pytest.fixture
# def prep():
#     Guitarist()
#     Bassist() 
#     Drummer()   

def test_version():
    assert __version__ == '0.1.0'
