import requests

# Creating a synthetic database, in the real world this might real database
database = {
    1: "Madhu",
    2: "Kiran",
    3: "Ravi"
}


def get_user_from_db(user_id):
    return database.get(user_id)


def get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    else:
        raise requests.exceptions.HTTPError(f"HTTPError: {response.status_code}")