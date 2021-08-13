def main():
    """
    This program tells how to write into a file using write and
    writelines methods
    """
    wish = "Hello ", "World"
    text = "Welcome to this world"
    write_file = open("write_exe.txt", "w")
    # write() method expects a single string as argument
    # If you want to see the difference pass wish variable instead of text
    write_file.write(text)
    # writelines() method expect an iterable of string as an argument
    write_file.writelines(wish)
    write_file.close()


if __name__ == '__main__':
    main()
