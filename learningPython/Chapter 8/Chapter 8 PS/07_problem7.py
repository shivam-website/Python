
def remov(list,word):
    n = []
    for item in list:
        if item != word:
            n.append(item.strip(word))  
    return n

list = ["Shivam","Rohan","Sohan","An","Rahul"]
print(remov(list,"An"))

 