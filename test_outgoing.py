import unittest

from enum import Enum

class OutgoingType(Enum):
    HOUSE = "HOUSE"
    CAR = "CAR"
    SAVINGS = "SAVINGS"
    OTHER = "OTHER"

class Outgoing:
    def __init__(self, outgoing_type, amount, payee, desc=""):
        self.outgoing_type = outgoing_type
        self.amount = amount
        self.desc = desc
        self.payee = payee

    def to_csv_row_str(self):
        return f"\"{self.outgoing_type.value}\",{self.amount:.2f},\"{self.payee}\",\"{self.desc}\""

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
