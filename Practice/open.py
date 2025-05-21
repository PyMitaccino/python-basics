with open("text.txt", "r") as file:
    last_line = file.readlines()
    print(last_line[:3])
