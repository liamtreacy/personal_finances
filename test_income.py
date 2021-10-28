import unittest

from enum import Enum


class IncomeType(Enum):
    WORK = "WORK"
    OTHER = "OTHER"

class PayeeName(Enum):
    LIAM = "Liam"
    CHRISTY = "Christy"

class Income:
    def __init__(self, income_type, amount, payee, desc=""):
        self.income_type = income_type
        self.amount = amount
        self.desc = desc
        self.payee = payee

    def to_csv_row_str(self):
        return f"\"{self.income_type.value}\",{self.amount:.2f},\"{self.payee.value}\",\"{self.desc}\""


class IncomeTestCase(unittest.TestCase):
    def test_income_creation(self):
        income = Income(IncomeType.WORK, 2500.00, PayeeName.CHRISTY, "Via bank transfer")

        self.assertEqual(income.amount, 2500.00)
        self.assertEqual(income.income_type, IncomeType.WORK)
        self.assertEqual(income.payee, PayeeName.CHRISTY)
        self.assertEqual(income.desc, "Via bank transfer")

    def test_income_creation_no_desc(self):
        income = Income(IncomeType.WORK, 1200.20, PayeeName.LIAM)

        self.assertEqual(income.amount, 1200.20)
        self.assertEqual(income.income_type, IncomeType.WORK)
        self.assertEqual(income.payee, PayeeName.LIAM)
        self.assertEqual(income.desc, "")

    def test_income_csv_row_str(self):
        income = Income(IncomeType.WORK, 1200.20, PayeeName.LIAM)

        self.assertEqual(income.to_csv_row_str(),"\"WORK\",1200.20,\"Liam\",\"\"")


if __name__ == '__main__':
    unittest.main()
