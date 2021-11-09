import unittest

from src.csv_reader import CsvReader


def get_dir_of_this_file():
    import os
    return os.path.dirname(os.path.abspath(__file__))


def get_standards_file():
    return get_dir_of_this_file() + '/../../house_spending_data_entry/standards/standards_one.csv'


class MyTestCase(unittest.TestCase):
    def test_something(self):
        c = CsvReader()
        net = c.read(get_standards_file())
        self.assertEqual(net, 3248.21)


if __name__ == '__main__':
    unittest.main()
