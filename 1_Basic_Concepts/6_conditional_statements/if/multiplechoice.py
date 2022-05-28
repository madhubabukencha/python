def main():
    choice = dict(
        n1="madhu",
        n2="ravi",
        n3="amma")
    name1 ="n5"
    name2 ="n1"
    print(choice.get(name1, "not found"))
    print(choice.get(name2, "not found"))


if __name__ == '__main__':
    main()
