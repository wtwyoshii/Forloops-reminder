list1 = [1, 6, 3]
list2 = ['a', 'b', 'c']

cartesian_product = []

for item1 in list1:
    for item2 in list2:
        cartesian_product.append((item1, item2))
        
for pair in cartesian_product:
    print(pair)