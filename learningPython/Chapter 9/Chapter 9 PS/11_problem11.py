with open("old.txt") as f:
    data = f.read()
    
with open("ranamed_by_python.txt","w") as f:
    f.write(data)