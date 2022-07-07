with open("result.txt", "w") as file:
    while True:
        s = input("Enter:")
        if not s:
            break
        file.write(s+"\n")
print("Done")