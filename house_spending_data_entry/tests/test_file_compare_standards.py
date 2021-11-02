import unittest

from src.csv_builder import CsvEntry, FlowType, write_entries_to_file
from src.money_area import MoneyAreaEnum
from src.payee_name import PayeeNameEnum


def remove_tmp_directory():
    import os
    if os.path.exists('../tmp/'):
        import shutil
        shutil.rmtree('../tmp/')

def get_tmp_dir_file_tuple():
    return ('../tmp/','tmp.csv')

def get_tmp_file():
    return '../tmp/tmp.csv'

def get_standards_file():
    return '../standards/standards_one.csv'

class FileCompareStandardsCase(unittest.TestCase):
    def test_not_a_unit_test_but_compare_output_file_against_standards(self):
        csv_entries = []

        csv_entries.append(CsvEntry(FlowType.OUTGOING, MoneyAreaEnum.OTHER, 2.34, PayeeNameEnum.OTHER))
        csv_entries.append(CsvEntry(FlowType.OUTGOING, MoneyAreaEnum.SAVINGS, 50.00, PayeeNameEnum.OTHER, "Rainy day fund"))
        csv_entries.append(CsvEntry(FlowType.INCOME, MoneyAreaEnum.WORK, 800.45, PayeeNameEnum.LIAM, "Bank, transfer"))
        csv_entries.append(CsvEntry(FlowType.INCOME, MoneyAreaEnum.WORK, 2500.10, PayeeNameEnum.CHRISTY, "Via lodged cheque"))

        # delete tmp/tmp.csv
        remove_tmp_directory()

        write_entries_to_file(csv_entries,get_tmp_dir_file_tuple())

        import filecmp
        result = filecmp.cmp(get_standards_file(), get_tmp_file())

        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()

