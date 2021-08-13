password = "madhu..."
count = 0
verify = ""
while verify != password:
    verify = input("Enter password:")
    if verify != password:
        count += 1
    else:
        continue
    if count == 3:
        print("Your account is blocked due to 3 times wrong entry")
        break
else:
    print("Hey Welcome")
