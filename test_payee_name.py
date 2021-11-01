import unittest

from enum import Enum

class PayeeNameEnum(Enum):
    __order__ = 'LIAM CHRISTY OTHER'
    LIAM = 0
    CHRISTY = 1
    OTHER = 2

def PayeeNameEnumToString(payee_name_enum):
    if payee_name_enum == PayeeNameEnum.LIAM:
        return "Liam"
    if payee_name_enum == PayeeNameEnum.CHRISTY:
        return "Christy"
    if payee_name_enum == PayeeNameEnum.OTHER:
        return "Other"

def StringtoPayeeNameEnum(payee_str):
    if payee_str.lower() == "liam":
        return PayeeNameEnum.LIAM
    if payee_str.lower() == "christy":
        return PayeeNameEnum.CHRISTY
    if payee_str.lower() == "other":
        return PayeeNameEnum.OTHER

def get_payee_name_from_user():
    for val in PayeeNameEnum:
        print(f"{val.key} , {val.value}")

class MyTestCase(unittest.TestCase):
    def test_something(self):
        get_payee_name_from_user()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
