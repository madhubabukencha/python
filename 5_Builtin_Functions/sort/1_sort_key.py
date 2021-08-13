# Data
portfolio = [{'name': 'AA', 'date': '2007-06-11', 'share': 100, 'price': 32.2},
             {'name': 'IBM', 'date': '2007-05-13', 'share': 50, 'price': 91.0},
             {'name': 'CAT', 'date': '2006-09-23', 'share': 150, 'price': 83.44},
             {'name': 'MSFT', 'date': '2007-05-17', 'share': 200, 'price': 21.23},
             {'name': 'GE', 'date': '2006-02-01', 'share': 95, 'price': 40.37},
             {'name': 'MSFT', 'date': '2006-10-31', 'share': 50, 'price': 65.1},
             {'name': 'IBM', 'date': '2006-07-09', 'share': 100, 'price': 70.44}]


# Function required to give the key
def holding_name(holding):
    return holding['name']


portfolio.sort(key=holding_name)
for record in portfolio:
    print(record)
