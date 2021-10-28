import unittest

from enum import Enum

class FlowType(Enum):
    INCOME = "INCOME"
    OUTGOING = "OUTGOING"

class CsvBuilder:
    def __init__(self):
        self.header_row = ["FlowType,SourceType,Amount,Payee,Desc"]
        self.rows = []

    def add_income(self, income_csv_row_str):
        self.rows.append(f"{FlowType.INCOME.value}"+income_csv_row_str)

    def add_outgoing(self, outgoing_csv_row_str):
        self.rows.append(f"{FlowType.OUTGOING.value}"+outgoing_csv_row_str)

    def build(self):
        return ','.join(self.header_row + self.rows)

class CsvBuilderTestCase(unittest.TestCase):
    def test_creation(self):
        c = CsvBuilder()
        self.assertEqual(c.build(), str(c.header_row[0]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
