strings = ["apple", "sample", "temple"]

def find_longest_suffix(strings):
    shortest = min(strings, key=len)
    common_suffix = ""

    for i in range(1, len(shortest) + 1):
        suffix = shortest[-i]

        if all(string.endswith(suffix) for string in strings):
            common_suffix = suffix
        else:
            break
    return common_suffix

result = find_longest_suffix(strings)
print("Largest suffix:", result)