import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1: #O(n)
#     for name_2 in names_2: #O(n)
#         if name_1 == name_2:
#             duplicates.append(name_1)
# Current Code Runtime = O(n^2)

# create a new bst at the middle of names_1
namesTree = BinarySearchTree(names_1[len(names_1) // 2]) #O(1)
for names_1 in names_1: #O(n)
    namesTree.insert(names_1) #O(log(n)) 
for names_2 in names_2: #O(n)
    if namesTree.contains(names_2): # O(log(n))
        duplicates.append(names_2) #O(1)
# New Code Runtime: O(2nlog(n))=> O(nlog(n))
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


# By implementing a binary search tree with the values of list 1, we are able to 
# cut down on the number of comparisons to the minimum, leaving our improved function running at O(n*log(n))