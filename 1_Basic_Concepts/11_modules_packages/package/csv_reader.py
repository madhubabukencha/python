import csv


def read_csv(filename, types, *, errors="warn"):
    """
    Read a CSV file with types conversion
    :param filename: "portfolio.csv"
    :param errors:"warn"
    :return:
    """
    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("Errors must be of 'warn' or 'silent', 'raise'")
    records = []
    with open(filename, "r") as my_data:
        rows = csv.reader(my_data)
        # print(type(rows))
        headers = next(rows)
        for row_number, row in enumerate(rows, start=1):
            try:
                row = [func(value) for func, value in zip(types, row)]
            except ValueError as err:
                if errors == 'warn':
                    print(f"Row : {row_number} , bad row : {row}")
                    print(f"Row : {row_number}, Reason: {err}")
                elif errors == 'raise':
                    raise
                else:
                    pass
                continue
            record = dict(zip(headers, row))
            records.append(record)
        return records
