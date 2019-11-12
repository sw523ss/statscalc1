import unittest
from Statistics.Statistics import Statistics
from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)


if __name__ == '__main__':
    unittest.main()
