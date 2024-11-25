word = "abc"

print("All possible character strings:")
for i in range(len(word)):
    for j in range(len(word)):
        for k in range(len(word)):

            print(word[i], word[j], word[k])