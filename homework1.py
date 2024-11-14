words = ["listen", "silent", "enlist", "abc", "cab"]

# for i in range(len(words)):

#     for j in range(i + 1, len(words)):
 
#         if sorted(words[i]) == sorted(words[j]):
#             print(f"({words[i]}, {words[j]})")

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if sorted(words[i]) == sorted(words[j]):
            print(f"({words[i]}, {words[j]})")
        
