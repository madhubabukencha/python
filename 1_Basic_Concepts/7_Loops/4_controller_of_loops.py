"""
Name : Madhu Babu Kencha

This program tells the usage of else, continue and break
"""


def loop_controllers():
    text = "This is string"
    text_index = 0
    
    while text_index < len(text):
        print(text[text_index], end="")
        text_index += 1
    # Once while statement False then else block will execute
    else:
        print("\nIteration is over")

    # Usage of "continue"
    for h in text:
        # Once you found 's' stop executing further statements
        # and go to the top and loops over on remaining elements
        if h == 's':
            continue
        print(h, end="")
    print()

    # Usage of "break"
    name = "madhu babu kencha"
    for h in name:
        # Once you found "u" break the loops
        if h == 'u':
            break    
        print(h, end="")


if __name__ == "__main__":
    loop_controllers()
