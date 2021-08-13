### HAVING SOME ISSUE######
## link : https://napuzba.com/a/import-error-relative-no-parent
# from . import csv_reader  # relative import

# For now continuing with normal import
import csv_reader


def read_portfolio(filename, *, errors="warn"):
    types = [str, str, int, float]
    return csv_reader.read_csv(filename, types)


if __name__ == '__main__':
    portfolio = read_portfolio("portfolio.csv", errors="warn")
    # print(portfolio)
    total = 0.0

    for holding in portfolio:
        total += holding['shares'] * holding['price']
    print("total : %f" % total)
