from enum import Enum

class PayeeNameEnum(Enum):
    __order__ = 'OTHER LIAM CHRISTY LOUISA'
    OTHER = 0
    LIAM = 1
    CHRISTY = 2
    LOUISA = 3

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