def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 500 | 502 | 501:
            return "Not allowed"
        case _:  # This is the default case
            return f"Something went wrong, https error code: {status}"


print(http_error(300))
print(http_error(400))
print(http_error(500))