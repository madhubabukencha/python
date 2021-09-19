def main():
    n = 1
    print("First call")
    yield n

    n += 1
    print("Second Call")
    yield n

    n += 1
    print("Third call")
    yield n


for i in main():
    print(i)
