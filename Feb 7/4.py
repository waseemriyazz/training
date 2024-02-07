# 4.Write a Python program to ask how many elements users want to create in a list, then let the user create 2 lists with the number of elements previously entered. Then create and display all combinations of letters, selecting each letter from a different key in a dictionary, and place all these combinations in a new list. Example: How many elements? 2 List 1 = ['a', 'b'] List 2 = ['c','d'] Output: newlist = [ac, ad, bc, bd]
number_of_elements = int(input("Enter the numnber of elements : "))
list1 = []
for i in range(0, number_of_elements):
    x = input(f"Enter element {i+1} of list 1 : ")
    list1.append(x)
list2 = []
for i in range(0, number_of_elements):
    x = input(f"Enter element {i+1} of list2 : ")
    list2.append(x)

newlist = []
for i in list1:
    for j in list2:
        element = i+j
        newlist.append(element)

print(newlist)
