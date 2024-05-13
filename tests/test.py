import pytest

from app.calc import Calculator


class Testcalc:

    # Инициализируем приложение калькулятор
    def setup(self):
        self.calc = Calculator

    # Проверяем умножение
    def test_multiply_succes(self):
        assert self.calc.multiply(self, 2, 2) == 4

    # Проверяем деление
    def test_division_succes(self):
        assert self.calc.division(self, 6, 2) == 3

    # Проверяем деление на ноль
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    # Проверяем вычетание
    def test_subtraction_succes(self):
        assert  self.calc.subtraction(self, 4, 2) == 2

    # Проверяем сложение"
    def test_adding_succes(self):
        assert self.calc.adding(self, 1, 1) == 2

    def teardown(self):
        print("Выполнение метода Teardown")
