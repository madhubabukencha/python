"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given scores. Store them in a list and find the score of the runner-up.
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""


def main():
    n = int(input())
    arr = []
    if n <= 10:
        for i in range(1, n+1):
            n = int(input())
            arr.append(i)
            arr.sort(reverse=True)  # arranging descending order
    print(arr[2])


if __name__ == '__main__':
    main()
