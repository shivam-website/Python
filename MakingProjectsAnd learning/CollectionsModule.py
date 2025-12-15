from collections import Counter

data = [1,1,2,2,3,3,3,4,4,4,4]
c = Counter(data)

print(c)
print(c.most_common(2))
