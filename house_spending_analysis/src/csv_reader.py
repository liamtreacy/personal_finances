class CsvReader:
    def __init__(self):
        self.csv_entries = []

    def read(self, csv_file):
        import csv
        total_income = 0.0
        total_outgoing = 0.0
        with open(csv_file) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row['FlowType'] == 'INCOME':
                    total_income += float(row['Amount'])
                elif row['FlowType'] == 'OUTGOING':
                    total_outgoing += float(row['Amount'])

        return total_income - total_outgoing