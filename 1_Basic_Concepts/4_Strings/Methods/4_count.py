def count_string(string, sub="", start=None, end=None):
    """
    Count method returns number of occurrence of substring
    in the specified range [start,end]. Optional arguments starts and
    ends are interpreted as in slice notation.
    Syntax:
    ------
    string.count(substring_name,start,end)

    Parameters:
    ----------
    string  The string name that you want to search
    start   Starting index(Optional)
    end     Ending index(Optional)

    :returns
    Return the occurrence of specified sub string in specified range
    """
    count = string.count(sub, start, end)
    print('Total number of i\'s in the complete text:%d' % count)


if __name__ == '__main__':
    message = "The most beautiful day in my life"
    count_string(message, "i")
    count_string(message, "i", 1, 28)
