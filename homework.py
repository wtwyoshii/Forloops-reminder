# scores = [[80, 90, 100], [70, 85, 90]]

# for i in range(len(scores)):
#     student_scores = scores[i]
#     average_score = sum(student_scores) / len(student_scores)
    

#     print(f"Student {i+1}: {average_score:.2f}")

# Solution 2:

scores = [[80, 90, 100], [70, 85, 90], [88, 76, 92]]

for i in range(len(scores)):
    total = 0
    student_scores = scores[i]

    for score in student_scores:
        total += score
    

    average_score = total / len(student_scores)

    print(f"Student {i+1}: {average_score:.2f}")