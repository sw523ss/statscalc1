import unittest
from Statistics.Statistics import Statistics
from CSVReader.CsvReader import CsvReader
from Calculator.Calculator import Calculator
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        test_data = CsvReader('Tests/Data/Unit_Test_Statistics.csv').data
        for row in test_data:
            result = float(row['mean1'])
            self.assertEqual(self.statistics.mean(row['ds1_value1'], row['ds1_value2'], row['ds1_value3'],
                                                  row['ds1_value4'], row['ds1_value5'], row['ds1_value6'],
                                                  row['ds1_value7'], row['ds1_value8'], row['ds1_value9'],
                                                  row['ds1_value10']), result)
            self.assertEqual(self.statistics.result, result)
            pprint(test_data)


if __name__ == '__main__':
    unittest.main()
