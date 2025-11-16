import random as r
import string as s

passLen = 12
allChars = s.ascii_letters + s.digits + s.punctuation
password ="".join(r.sample(allChars,passLen))
print("Your secure password is:", password)
