from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from CSVReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result

