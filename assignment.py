 #Given two lists of words, use nested for loops to generate and print all possible pairs, one word from each list. For example, pairing ["apple", "banana"] with ["red", "yellow"] should print apple-red, apple-yellow, etc.
list1 = ['apple', 'banana']
list2 = ['red', 'yellow' ]

for word1 in list1:
    for word2 in list2:
        print(word1, word2)