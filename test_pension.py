import unittest


class Investment:
    def __init__(self, name="", unit_amount=0.0, unit_price=0.0):
        self.name = name
        self.unit_amount = unit_amount
        self.unit_price = unit_price

    def cost(self):
        return self.unit_amount * self.unit_price


class TestInvestment(unittest.TestCase):
    def setUp(self):
        self.name = "TEsts"


class TestInit(TestInvestment):
    def test_investment_setup(self):
        contrb = Investment("S&P 500 ETF", 2.0, 200.00)
        self.assertEqual(contrb.name, "S&P 500 ETF")
        self.assertEqual(contrb.unit_amount, 2.0)
        self.assertEqual(contrb.unit_price, 200.0)
        self.assertEqual(contrb.cost(), 400)
