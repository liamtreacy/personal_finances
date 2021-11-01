import unittest

from enum import Enum

class PayeeNameEnum(Enum):
    __order__ = 'OTHER LIAM CHRISTY'
    OTHER = 0
    LIAM = 1
    CHRISTY = 2

def number_to_payee(num):
    return PayeeNameEnum(num)

def payee_to_string(payee_name_enum):
    return payee_name_enum.name

def string_to_payee(payee_str):
    return PayeeNameEnum[payee_str.upper()]

def print_payee_names_and_values():
    str = ""
    for val in PayeeNameEnum:
        str +=f"{val.value} for {val.name} : "
    print(str)

class PayeeEnumAndFunctionsTestCase(unittest.TestCase):
    def test_PayeeNameEnum_creation_from_number_other(self):
        self.assertEqual(PayeeNameEnum.OTHER, number_to_payee(0))

    def test_PayeeNameEnum_creation_from_number_christy(self):
        self.assertEqual(PayeeNameEnum.CHRISTY, number_to_payee(2))

    def test_PayeeNameEnum_creation_from_string_other(self):
        self.assertEqual(PayeeNameEnum(0), string_to_payee('OTHER'))

    def test_PayeeNameEnum_creation_from_string_christy_lower(self):
        self.assertEqual(PayeeNameEnum(2), string_to_payee('christy'))

    def test_PayeeNameEnum_creation_from_string_christy_mixed(self):
        self.assertEqual(PayeeNameEnum(2), string_to_payee('ChriSty'))

    def test_Payee_to_string(self):
        self.assertEqual("LIAM", payee_to_string(PayeeNameEnum(1)))

if __name__ == '__main__':
    unittest.main()
