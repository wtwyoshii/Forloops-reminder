#Write a program that takes two lists and uses nested for loops to find all common elements between them.
list1 = [1, 2, 3, 4, 5, 7, 8]
list2 = [4, 6, 8, 10, 7]

common_elements = []

for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            print(item1)
            