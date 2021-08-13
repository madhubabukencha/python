def casefold_string(string):
    """
    The casefold() method removes all case distinctions present in a string
    It is used for caseless matching, i.e. ignores cases when comparing.

    The casefold() method is an aggressive lower() method which converts
    strings to case folded strings for caseless matching.

    For example, the German lowercase letter ß is equivalent to ss. However,
    since ß is already lowercase, the lower() method does nothing to it. But,
    casefold() converts it to ss.
    Syntax:
    ------
    string.casefold()

    :returns
    casefold(small case letters) string
    """
    casefold_str = string.casefold()
    lower_str = string.lower()
    print(f"CaseFold String: {casefold_str}")
    print(f"Lowercase String: {lower_str}\n")


if __name__ == '__main__':
    messages = ["PYTHON IS VERY BEST LANGUAGE", "%% jdks Tho kksRRRs", "ß"]
    messages.reverse()
    for message in messages:
        print(f"Original String: {message}")
        casefold_string(message)
