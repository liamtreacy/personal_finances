import unittest

from src.money_area import MoneyAreaEnum, number_to_money_area, string_to_money_area, money_area_to_string


class MoneyAreaEnumAndFunctionsTestCase(unittest.TestCase):
    def test_MoneyAreaEnum_creation_from_number_other(self):
        self.assertEqual(MoneyAreaEnum.OTHER, number_to_money_area(0))

    def test_MoneyAreaEnum_creation_from_number_rec(self):
        self.assertEqual(MoneyAreaEnum.RECREATION, number_to_money_area(9))

    def test_MoneyAreaEnum_creation_from_string_other(self):
        self.assertEqual(MoneyAreaEnum(0), string_to_money_area('OTHER'))

    def test_MoneyAreaEnum_creation_from_string_car_lower(self):
        self.assertEqual(MoneyAreaEnum(3), string_to_money_area('car'))

    def test_MoneyAreaEnum_creation_from_string_car_mixed(self):
        self.assertEqual(MoneyAreaEnum(3), string_to_money_area('CAr'))

    def test_MoneyArea_to_string(self):
        self.assertEqual("GROCERIES", money_area_to_string(MoneyAreaEnum(5)))


if __name__ == '__main__':
    unittest.main()
