from src.mathoperations import add,subtract

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0 #assert return true if condition holds true

def test_sub():
    assert subtract(4,1) == 3
    assert subtract(4,3) == 1