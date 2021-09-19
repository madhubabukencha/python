"""
In this program we are going to see how to use yield statement with for loop
"""


def main(text):
    length = len(text)
    # >>> n=5;list(range(n-1, -1, -1))
    # [4, 3, 2, 1, 0]
    for i in range(length-1, -1, -1):
        yield text[i]


word = main("Madhu")
print(next(word))
print(next(word))
print(next(word))
print(next(word))
print(next(word))
print(next(word))

