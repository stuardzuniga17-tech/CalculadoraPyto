import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(calculator.suma(3, 2), 5)

    def test_resta(self):
        self.assertEqual(calculator.resta(5, 3), 2)

    def test_multiplica(self):
        self.assertEqual(calculator.multiplica(4, 3), 12)

if __name__ == '__main__':
    unittest.main()