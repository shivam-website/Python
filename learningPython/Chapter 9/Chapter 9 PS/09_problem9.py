with open("this.txt") as f:
    data1 = f.read()
with open("poem.txt") as f:
    data2 = f.read()
if(data1==data2):
    print("Files are identical")
else:
    print("Files are not identical")