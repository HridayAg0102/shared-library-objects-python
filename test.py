# test_calculator.py
from libcalculator.add import add
from libcalculator.subtract import subtract

def test_add():
    result = add(3, 4)
    assert result == 7, f"Expected 7, but got {result}"

def test_subtract():
    result = subtract(7, 2)
    assert result == 5, f"Expected 5, but got {result}"

if __name__ == "__main__":
    test_add()
    test_subtract()

    print("All tests passed!")
