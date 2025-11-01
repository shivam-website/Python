fruits = ["Apple","Orange",7,True]
print(fruits)
fruits.append("Litchi")
print(fruits)
fruits.extend(["Banana", "Mango"])
print(fruits)  
print(len(fruits))  # Example: 4 #gives the num of elements in the list


l1 = [1,92,85,72,23]
# l1.sort() 
# print(l1)
# l1.reverse()
# l1.insert(1,5)#insert 5 at the 1 index
# l1.pop(2) #remove the value from the index given
# l1.remove(72)#remove a particular value
print(l1)

nums = [1, 2, 2, 3, 2, 4] 
print(nums.count(2))  # Output: 3 #how many times the same num is repeating

names = ["Shivam", "Aarav", "Shivam"]
print(names.index("Shivam"))  # Output: 0 #finds the index of the given element


#Makes a shallow copy of the list (so changing one doesn’t affect the other).
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(type(a))  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]

#clear all the elements from the list
x = [1, 2, 3]
x.clear()
print(x)  # []

#Sorts in ascending (default) or descending (if reverse=True) order.
l1 = [5, 2, 8, 1]
l1.sort(reverse=True)
print(l1)  # [8, 5, 2, 1]
