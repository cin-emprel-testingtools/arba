import pytest
from src.calculator import Calculator

class TestCalculator():

    def setup_class(self):
        self.calc = Calculator()
        print("\n setup_class() before any methods in this class");

    def teardown_class(self):
        print("\n teardown_class() after any methods in this class");

    def test_addition(self):
        assert self.calc.addition(2,2) == 4

    def test_subtraction(self):
        assert self.calc.subtraction(2,2) == 0

    @pytest.mark.skip(reason="Duplicated test")
    def test_multipication(self):
        assert self.calc.multipication(2,2) == 4
    
    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(10,0)