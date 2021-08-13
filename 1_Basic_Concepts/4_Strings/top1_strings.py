"""
1)A string is sequence of characters. A character is just a symbol
2)Even-though we are able to see the character on scree, computer stores
  them internally in 0's and 1's
3)The process of converting a character to number is call encoding.
  And the process process called decoding
4)In python, a string is a sequence of unicode character. Unicode was
  introduced to include every character in all languages and to bring
  uniformity in encoding.
"""


def decoration(func):
    CEND = '\33[0m'
    CYELLOWBG2 = '\33[103m'
    # To use function variable outside
    end_line = 35*"*"
    if func == quotes:
        print(CYELLOWBG2 + "Printing statements in different ways" + CEND)
        quotes()
        print(end_line)
    elif func == accessing:
        print(CYELLOWBG2 + "Different ways to access strings" + CEND)
        accessing()
        print(end_line)


def quotes():
    # creation of strings
    var1 = 'Single quotes'
    var2 = "Double quotes"
    var3 = '''The most amazing 
              journey'''
    var4 = """I love python"""
    for var in [var1, var2, var3, var4]:
        print(var)


def accessing():
    name = "Madhu Babu Kencha"
    print("name=%s" % name)
    print("name[:]=", name[:])
    print("name[3:]=", name[3:])
    print("name[6:-1]=", name[6:-1])
    print("name[::-1]=", name[::-1])


if __name__ == '__main__':
        decoration(quotes)
        decoration(accessing)
