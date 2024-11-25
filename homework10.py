birth_years = [1990, 1985, 200, 1995]

for i in range(len(birth_years)):
    for j in range(i + 1, len(birth_years)):
        age_difference = abs(birth_years[i] - birth_years[j])
        print(f"Age difference between person {i+1} (born {birth_years[i]}) and person {j+1} (born {birth_years[j]}): {age_difference} years")