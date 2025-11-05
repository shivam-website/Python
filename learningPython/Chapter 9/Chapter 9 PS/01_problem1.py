with open("poem.txt") as f:
    data = f.read()
    if("Twinkle" in data):
        print("Twinkle is present")
    else:
        print("Twinkle is not present")
    # print(data)