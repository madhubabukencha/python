"""
Requirement: python 3.10

In Python, a 'match-case' is equivalent to a 'switch-case'
statement in other programming languages.
"""

code = int(input("Enter error code: "))

match code:
    case 200:
        print("The request is OK")
    case 400:
        print("The server did not understand the request")
    case 500:
        print("The request was not completed, the server met unxpected error")
    case _:
        print(f"For {code}: Error is unknow")


def main():
    print("Hello World")


