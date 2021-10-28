import unittest

from enum import Enum

from test_income import Income, IncomeType, PayeeName
from test_outgoing import Outgoing, OutgoingType


class FlowType(Enum):
    INCOME = "INCOME"
    OUTGOING = "OUTGOING"

class CsvBuilder:
    def __init__(self):
        self.header_row = ["FlowType,SourceType,Amount,Payee,Desc"]
        self.rows = []

    def add_income(self, income):
        self.rows.append(f"{FlowType.INCOME.value},"+income.to_csv_row_str())

    def add_outgoing(self, outgoing):
        self.rows.append(f"{FlowType.OUTGOING.value},"+outgoing.to_csv_row_str())

    def build(self):
        return '\n'.join(self.header_row + self.rows)

class CsvBuilderTestCase(unittest.TestCase):
    def test_creation(self):
        c = CsvBuilder()
        self.assertEqual(c.build(), str(c.header_row[0]))

    def test_add_income(self):
        c = CsvBuilder()
        i = Income(IncomeType.WORK, 2500.10, PayeeName.CHRISTY, "Via lodged cheque")
        c.add_income(i)

        expected_str = "FlowType,SourceType,Amount,Payee,Desc\nINCOME,\"WORK\",2500.10,\"Christy\",\"Via " \
                       "lodged cheque\""
        self.assertEqual(c.build(), expected_str)

    def test_add_multiple_incomes(self):
        c = CsvBuilder()
        i = Income(IncomeType.WORK, 2500.10, PayeeName.CHRISTY, "Via lodged cheque")
        j = Income(IncomeType.WORK, 800.45, PayeeName.LIAM, "Bank, transfer")
        c.add_income(i)
        c.add_income(j)

        expected_str = "FlowType,SourceType,Amount,Payee,Desc\nINCOME,\"WORK\",2500.10,\"Christy\",\"Via " \
                       "lodged cheque\"\nINCOME,\"WORK\",800.45,\"Liam\",\"Bank, transfer\""
        self.assertEqual(c.build(), expected_str)

    def test_add_outgoing(self):
        c = CsvBuilder()
        i = Outgoing(OutgoingType.HOUSE, 102.34, "Boiler", "Cash in hand")
        c.add_outgoing(i)

        expected_str = "FlowType,SourceType,Amount,Payee,Desc\nOUTGOING,\"HOUSE\",102.34,\"Boiler\",\"Cash " \
                       "in hand\""
        self.assertEqual(c.build(), expected_str)

    def test_add_multiple_outgoings(self):
        c = CsvBuilder()
        i = Outgoing(OutgoingType.OTHER, 2.34, "Co-op")
        j = Outgoing(OutgoingType.SAVINGS, 50.00, "Regular savings", "Rainy day fund")
        c.add_outgoing(i)
        c.add_outgoing(j)

        expected_str = "FlowType,SourceType,Amount,Payee,Desc\nOUTGOING,\"OTHER\",2.34,\"Co-op\",\"\"\nOUTGOING," \
                       "\"SAVINGS\",50.00,\"Regular savings\",\"Rainy day fund\""
        self.assertEqual(c.build(), expected_str)

if __name__ == '__main__':
    unittest.main()
