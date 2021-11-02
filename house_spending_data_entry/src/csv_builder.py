from enum import Enum

from src.money_area import print_money_area_names_and_values, number_to_money_area
from src.payee_name import print_payee_names_and_values, number_to_payee

class FlowType(Enum):
    INCOME = "INCOME"
    OUTGOING = "OUTGOING"

def get_payee():
    print("Enter the number corresponding to the Payee")
    print_payee_names_and_values()
    payee_num = int(input("> "))
    return number_to_payee(payee_num)

def get_payee():
    print("Enter the number corresponding to the Payee")
    print_payee_names_and_values()
    payee_num = int(input("> "))
    return number_to_payee(payee_num)

def get_money_area():
    print("Enter the number corresponding to the MoneyArea")
    print_money_area_names_and_values()
    money_area_num = int(input("> "))
    return number_to_money_area(money_area_num)

class CsvEntry:
    def __init__(self, flow_type, money_area, amount, payee, desc=""):
        self.flow_type = flow_type
        self.money_area = money_area
        self.amount = amount
        self.desc = desc
        self.payee = payee

    def to_csv_row_str(self):
        return f"{self.flow_type.value},\"{self.money_area.name}\",{self.amount:.2f},\"{self.payee.name}\",\"{self.desc}\""

class CsvBuilder:
    def __init__(self):
        self.header_row = ["FlowType,SourceType,Amount,Payee,Desc"]
        self.rows = []

    def add_entry(self, csv_entry):
        self.rows.append(csv_entry.to_csv_row_str())

    def build(self):
        return '\n'.join(self.header_row + self.rows)

    def write_to_file(self, output_tuple):
        import pathlib
        pathlib.Path(output_tuple[0]).mkdir(parents=True, exist_ok=True)

        import os
        if not os.path.exists(output_tuple[0]+output_tuple[1]):
            text_file = open(output_tuple[0]+output_tuple[1], "w")
            text_file.write(self.build())
            text_file.close()
        else:
            print("File already exists!")

def write_entries_to_file(csv_entries, output_location):
    if len(csv_entries) == 0:
        print("No entries. Quitting.")
        return

    c = CsvBuilder()

    for x in csv_entries:
        c.add_entry(x)

    c.write_to_file(output_location)