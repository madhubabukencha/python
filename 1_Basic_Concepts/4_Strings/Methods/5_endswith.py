def main():
    """
    The endswith() method returns "True" if a string ends with the specified suffix
    If not returns the "False".

    Syntax:
    ------
    string.endswith(suffix,start,end)

    Parameters:
    ----------
    suffix  suffix that you want to check
    start   staring index to start searching from(inclusive)
    end     ending index to end the searching(exclusive)

    :returns
    It returns a boolean value("True" or "False")
    """
    text = "I am learning string methods."
    print(text.endswith("methods."))

    # start(0) is inclusive & end(20) is exclusive
    print(text.endswith("string", 0, 20))
    print(text.endswith("methods.", 0, 20))


if __name__ == '__main__':
    main()
