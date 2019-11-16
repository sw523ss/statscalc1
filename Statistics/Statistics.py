from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from CSVReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self):
        pass

    def mean(self, val1, val2, val3, val4, val5, val6, val7, val8, val9, val10):
        self.result = mean(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10)
        return self.result

