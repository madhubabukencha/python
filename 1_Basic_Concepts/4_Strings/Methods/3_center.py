def center_string(string, width, fill_char):
    """
    The center() method returns a string which is padded
    with the specified character
    Syntax:
    ------
    string.center(width,'fill_char')

    Parameters:
    ----------
    width      Length of the string with padded characters
    fill_char   Padding character,by default it provide space(optional)

    :returns
    Returns a padded string
    """
    padded_string = string.center(width, fill_char)
    print('Name of the lesson:', padded_string)
    print("The length of string of padding:", len(padded_string))


if __name__ == '__main__':
    title = ' The Python '
    center_string(title, 30, "#")
