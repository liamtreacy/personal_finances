from enum import Enum

from test_payee_name import print_payee_names_and_values, number_to_payee


class PayeeName(Enum):
    LIAM = "Liam"
    CHRISTY = "Christy"
    OTHER = "OTHER"

def PayeeNameToString(payee_name):
    return ""

class FlowType(Enum):
    INCOME = "INCOME"
    OUTGOING = "OUTGOING"

class MoneyArea(Enum):
    WORK = "WORK"
    OTHER = "OTHER"
    HOUSE = "HOUSE"
    CAR = "CAR"
    SAVINGS = "SAVINGS"
    GROCERIES = "GROCERIES"

def get_money_area():
    print("Select: 1 - Work, 2 - Other")
    return MoneyArea.WORK

def get_payee():
    print("Enter the number corresponding to the Payee")
    print_payee_names_and_values()
    payee_num = int(input("> "))
    return number_to_payee(payee_num)

class CsvEntry:
    def __init__(self, flow_type, money_area, amount, payee, desc=""):
        self.flow_type = flow_type
        self.money_area = money_area
        self.amount = amount
        self.desc = desc
        self.payee = payee

    def to_csv_row_str(self):
        return f"{self.flow_type.value},\"{self.money_area.value}\",{self.amount:.2f},\"{self.payee.value}\",\"{self.desc}\""

class CsvBuilder:
    def __init__(self):
        self.header_row = ["FlowType,SourceType,Amount,Payee,Desc"]
        self.rows = []

    def add_entry(self, csv_entry):
        self.rows.append(csv_entry.to_csv_row_str())

    def build(self):
        return '\n'.join(self.header_row + self.rows)

    def write_to_file(self, output_file):
        print(self.build(), file=open(output_file, 'w'))