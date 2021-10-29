from csv_builder import get_money_area, CsvBuilder, CsvEntry, get_payee, FlowType, MoneyArea


def generate_file_name(month, year):
    return "../household_spending/" + year + "/" + month + ".csv"


if __name__ == '__main__':

    # Enter month and year
    #
    month = input("Enter month: ")
    year = input("Enter year: ")

    csv_entries = []

    # Loop:
    #   Get incomes
    #
    keep_looping = 'y'
    while keep_looping == 'y':
        keep_looping = input("Enter another income entry? (y/n) ")

        if keep_looping == 'y':
            # flow_type, money_area, amount, payee, desc=""):
            print("\n=== New Income Entry ===")
            money_area = get_money_area()
            amount = float(input("Enter amount: "))
            payee = get_payee()
            desc = input("Enter description (optional): ")
            csv_entries.append(CsvEntry(FlowType.INCOME, money_area, amount, payee, desc))
            print("======\n\n")

    # Loop:
    #   Get outgoings
    #
    keep_looping = 'y'
    while keep_looping == 'y':
        keep_looping = input("Enter another income entry? (y/n) ")

        if keep_looping == 'y':
            # flow_type, money_area, amount, payee, desc=""):
            print("\n=== New Income Entry ===")
            money_area = get_money_area()
            amount = float(input("Enter amount: "))
            payee = get_payee()
            desc = input("Enter description (optional): ")
            csv_entries.append(CsvEntry(FlowType.INCOME, money_area, amount, payee, desc))
            print("======\n\n")

    c = CsvBuilder()

    for x in csv_entries:
        c.add_entry(x)

    # Write to file
    #
    c.write_to_file(generate_file_name(month, year))
