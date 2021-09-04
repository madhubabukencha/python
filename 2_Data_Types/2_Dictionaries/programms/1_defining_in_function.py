company_details = {"name": "Tata Consultancey Service", "data": '24-02-2017',
                   "shares": 200, "price": 100}


def total_shares(x):
    print("Total company worth:", x["shares"] * x["price"])


if __name__ == "__main__":
    total_shares(company_details)
