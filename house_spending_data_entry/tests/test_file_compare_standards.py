import unittest

from src.csv_builder import CsvEntry, FlowType, write_entries_to_file
from src.money_area import MoneyAreaEnum
from src.payee_name import PayeeNameEnum


def get_dir_of_this_file():
    import os
    return os.path.dirname(os.path.abspath(__file__))


def remove_tmp_directory():
    import os
    if os.path.exists(get_dir_of_this_file() + '/../tmp/'):
        import shutil
        shutil.rmtree(get_dir_of_this_file() + '/../tmp/')


def get_tmp_dir_file_tuple():
    return (get_dir_of_this_file() + '/../tmp/', 'tmp.csv')


def get_tmp_file():
    return get_dir_of_this_file() + '/../tmp/tmp.csv'


def get_standards_file():
    return get_dir_of_this_file() + '/../standards/standards_one.csv'


class FileCompareStandardsCase(unittest.TestCase):
    def test_not_a_unit_test_but_compare_output_file_against_standards(self):
        csv_entries = []

        csv_entries.append(CsvEntry(FlowType.OUTGOING, MoneyAreaEnum.OTHER, 2.34, PayeeNameEnum.OTHER))
        csv_entries.append(
            CsvEntry(FlowType.OUTGOING, MoneyAreaEnum.SAVINGS, 50.00, PayeeNameEnum.OTHER, "Rainy day fund"))
        csv_entries.append(CsvEntry(FlowType.INCOME, MoneyAreaEnum.WORK, 800.45, PayeeNameEnum.LIAM, "Bank, transfer"))
        csv_entries.append(
            CsvEntry(FlowType.INCOME, MoneyAreaEnum.WORK, 2500.10, PayeeNameEnum.CHRISTY, "Via lodged cheque"))

        # delete tmp/tmp.csv
        remove_tmp_directory()

        write_entries_to_file(csv_entries, get_tmp_dir_file_tuple())

        s = open(get_standards_file(), "r")
        t = open(get_tmp_file(), "r")

        self.assertEqual(t.read(), s.read())


if __name__ == '__main__':
    unittest.main()
