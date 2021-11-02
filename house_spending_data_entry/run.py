from src.csv_builder import CsvEntry, get_payee, FlowType, get_money_area, write_entries_to_file

# Assumption that the repository for tracking the csv files is checked out in same
# root directory as the personal_finances repo.
household_budget_repository_location = "../../household_spending/"


def generate_file_name_and_location(month, year):
    return (household_budget_repository_location + year + "/", month + ".csv")


def get_month_year():
    month = input("Enter month: ")
    year = input("Enter year: ")
    return month, year


def get_money_flow(flow_type_enum):
    csv_entries = []
    keep_looping = 'y'
    while keep_looping == 'y':
        keep_looping = input(f"Enter another {flow_type_enum.name} entry? (y/n) ")

        if keep_looping == 'y':
            print(f"\n=== New {flow_type_enum.name} Entry ===")
            money_area = get_money_area()
            amount = float(input("Enter amount: "))
            payee = get_payee()
            desc = input("Enter description (optional): ")
            csv_entries.append(CsvEntry(flow_type_enum, money_area, amount, payee, desc))
            print("======\n\n")

    return csv_entries


def get_user_inputs():
    month_year = get_month_year()
    csv_entries = []

    csv_entries += get_money_flow(FlowType.INCOME)
    csv_entries += get_money_flow(FlowType.OUTGOING)

    write_entries_to_file(csv_entries, generate_file_name_and_location(month_year[0], month_year[1]))


if __name__ == '__main__':
    get_user_inputs()
