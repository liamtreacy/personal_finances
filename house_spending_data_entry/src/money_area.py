from enum import Enum


class MoneyAreaEnum(Enum):
    __order__ = 'OTHER WORK HOUSE CAR SAVINGS GROCERIES INVESTMENTS UTILITIES FINANCE RECREATION'
    OTHER = 0
    WORK = 1
    HOUSE = 2
    CAR = 3
    SAVINGS = 4
    GROCERIES = 5
    INVESTMENTS = 6
    UTILITIES = 7
    FINANCE = 8
    RECREATION = 9

def number_to_money_area(num):
    return MoneyAreaEnum(num)

def money_area_to_string(money_area):
    return money_area.name

def string_to_money_area(money_area_str):
    return MoneyAreaEnum[money_area_str.upper()]

def print_money_area_names_and_values():
    str = ""
    for val in MoneyAreaEnum:
        str += f"{val.value} for {val.name} : "
    print(str)