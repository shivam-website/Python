names = input("Enter names separated by commas: ").split(",")

sentence = "{} are great coders.".format(" and ".join(names))

print(sentence)
