import unittest

from src.payee_name import PayeeNameEnum, string_to_payee, payee_to_string, number_to_payee


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
