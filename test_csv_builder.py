import unittest

from csv_builder import CsvBuilder, CsvEntry, FlowType, MoneyArea, PayeeName


class CsvBuilderTestCase(unittest.TestCase):
    def test_creation(self):
        c = CsvBuilder()
        self.assertEqual(c.build(), str(c.header_row[0]))

    def test_add_income(self):
        c = CsvBuilder()
        c.add_entry( CsvEntry(FlowType.INCOME, MoneyArea.WORK, 2500.10, PayeeName.CHRISTY, "Via lodged cheque") )

        expected_str = "FlowType,SourceType,Amount,Payee,Desc\nINCOME,\"WORK\",2500.10,\"Christy\",\"Via " \
                       "lodged cheque\""
        self.assertEqual(c.build(), expected_str)

    def test_add_multiple_incomes(self):
        c = CsvBuilder()

        c.add_entry( CsvEntry(FlowType.INCOME, MoneyArea.WORK, 2500.10, PayeeName.CHRISTY, "Via lodged cheque") )
        c.add_entry( CsvEntry(FlowType.INCOME, MoneyArea.WORK, 800.45, PayeeName.LIAM, "Bank, transfer") )

        expected_str = "FlowType,SourceType,Amount,Payee,Desc\nINCOME,\"WORK\",2500.10,\"Christy\",\"Via " \
                       "lodged cheque\"\nINCOME,\"WORK\",800.45,\"Liam\",\"Bank, transfer\""
        self.assertEqual(c.build(), expected_str)

    def test_add_outgoing(self):
        c = CsvBuilder()
        c.add_entry( CsvEntry(FlowType.OUTGOING, MoneyArea.HOUSE, 102.34, PayeeName.OTHER, "Cash in hand") )

        expected_str = "FlowType,SourceType,Amount,Payee,Desc\nOUTGOING,\"HOUSE\",102.34,\"OTHER\",\"Cash " \
                       "in hand\""
        self.assertEqual(c.build(), expected_str)

    def test_add_multiple_outgoings(self):
        c = CsvBuilder()

        c.add_entry( CsvEntry(FlowType.OUTGOING, MoneyArea.OTHER, 2.34, PayeeName.OTHER) )
        c.add_entry( CsvEntry(FlowType.OUTGOING, MoneyArea.SAVINGS, 50.00, PayeeName.OTHER, "Rainy day fund") )

        expected_str = "FlowType,SourceType,Amount,Payee,Desc\nOUTGOING,\"OTHER\",2.34,\"OTHER\",\"\"\nOUTGOING," \
                       "\"SAVINGS\",50.00,\"OTHER\",\"Rainy day fund\""
        self.assertEqual(c.build(), expected_str)

    def test_multiple_income_and_outgoings(self):
        c = CsvBuilder()

        c.add_entry( CsvEntry(FlowType.OUTGOING, MoneyArea.OTHER, 2.34, PayeeName.OTHER) )
        c.add_entry( CsvEntry(FlowType.OUTGOING, MoneyArea.SAVINGS, 50.00, PayeeName.OTHER, "Rainy day fund") )
        c.add_entry( CsvEntry(FlowType.INCOME, MoneyArea.WORK, 800.45, PayeeName.LIAM, "Bank, transfer") )
        c.add_entry( CsvEntry(FlowType.INCOME, MoneyArea.WORK, 2500.10, PayeeName.CHRISTY, "Via lodged cheque") )

        expected_str = "FlowType,SourceType,Amount,Payee,Desc\nOUTGOING,\"OTHER\",2.34,\"OTHER\",\"\"\nOUTGOING," \
                       "\"SAVINGS\",50.00,\"OTHER\",\"Rainy day fund\"\nINCOME,\"WORK\",800.45,\"Liam\"," \
                       "\"Bank, transfer\"\nINCOME,\"WORK\",2500.10,\"Christy\",\"Via lodged cheque\""
        self.assertEqual(c.build(), expected_str)

if __name__ == '__main__':
    unittest.main()
