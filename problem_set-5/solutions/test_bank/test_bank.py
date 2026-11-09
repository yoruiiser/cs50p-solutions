from bank import value
def test1():
    assert value("hello")==0
    assert value("HELLO")==0
    assert value("HeLlo")==0

def test2():
    assert value("h")==20
    assert value("H")==20
    assert value("hi")==20

def test3():
    assert value("welcome")==100
    assert value("123")==100

