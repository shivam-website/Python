with open("this.txt","r") as f:
    data = f.read()
    
with open("this_copy.txt","w") as f:
    f.write(data)