def capitalize_word(*, string):
    """
    This method capitalizes only first character of string
    Syntax:
    -------
    string.capitalize()

    :returns
    Returns capitalized string
    """
    string = string.capitalize()
    print(string)


if __name__ == '__main__':
    capitalize_word(string="newton")
    capitalize_word(string="122newton")
