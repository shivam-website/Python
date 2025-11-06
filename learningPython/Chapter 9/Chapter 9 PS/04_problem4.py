word = "######"
with open("file.txt") as f:
    content = f.read()

contentNew = content.replace("Donkey",word)
with open("file.txt","w") as f:
    f.write(contentNew)