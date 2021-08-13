name = "Madhu Babu Kencha"


def user_name(user_name):
    print(f"User Name : {user_name}")


def second_function():
    print("user_name function calling from second_function")
    user_name(name)


second_function()
