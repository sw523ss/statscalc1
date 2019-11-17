import unittest
from Statistics.Statistics import Statistics
from CSVReader.CsvReader import CsvReader
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

    def test_median(self):
        test_data = CsvReader('Tests/Data/Unit_Test_Statistics.csv').data
        for row in test_data:
            result = float(row['median1'])
            self.assertEqual(self.statistics.median(row['ds1_value1'], row['ds1_value2'], row['ds1_value3'],
                                                    row['ds1_value4'], row['ds1_value5'], row['ds1_value6'],
                                                    row['ds1_value7'], row['ds1_value8'], row['ds1_value9']), result)
            self.assertEqual(self.statistics.result, result)

    def test_mode(self):
        test_data = CsvReader('Tests/Data/Unit_Test_Statistics.csv').data
        for row in test_data:
            result = float(row['mode1'])
            self.assertEqual(self.statistics.mode(row['ds1_value1'], row['ds1_value2'], row['ds1_value3'],
                                                  row['ds1_value4'], row['ds1_value5'], row['ds1_value6'],
                                                  row['ds1_value7'], row['ds1_value8'], row['ds1_value9'],
                                                  row['ds1_value10']), result)
            self.assertEqual(self.statistics.result, result)

    def test_variance(self):
        test_data = CsvReader('Tests/Data/Unit_Test_Statistics.csv').data
        for row in test_data:
            result = float(row['var1'])
            self.assertEqual(self.statistics.variance(row['ds1_value1'], row['ds1_value2'], row['ds1_value3'],
                                                      row['ds1_value4'], row['ds1_value5'], row['ds1_value6'],
                                                      row['ds1_value7'], row['ds1_value8'], row['ds1_value9'],
                                                      row['ds1_value10']), result)
            self.assertEqual(self.statistics.result, result)


if __name__ == '__main__':
    unittest.main()
