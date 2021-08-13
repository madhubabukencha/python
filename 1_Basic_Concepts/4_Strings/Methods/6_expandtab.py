def expandtabs(string, tab_size=None):
    """
    The expandtabs() method return a copy of string in which
    tab characters i.e '\t' are expended using spaces optionally
    the given tabsize is 8
    Syntax:
    ------
    string.expandtab(tab_size)

    :parameter
    tab_size  tab size

    :return
    The expandtabs() returns a string where all '\t' characters are replaced
    with whitespace characters until the next multiple of tabsize parameter.
    """
    result = string.expandtabs(tab_size)
    print(result)


if __name__ == '__main__':
    # If tab is present, 3rd, 6th, 9th, 12th, 15th position then only update
    # or else it will just update with single space.
    # If tab found at 2nd position it will update just one space and then count
    # 3 places and if it found it will update with 3 spaces
    expandtabs('012\t012\t01\t012\t23', tab_size=3)
    expandtabs('123\t456789012352\t78', tab_size=5)
