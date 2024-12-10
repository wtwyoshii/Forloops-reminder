def find_palindrom(strings):
    for string in strings:
        print(f"{string}")
        n = len(string)
        for i in range(n):
            for j in range(i,n):
                substring = string[i:j + 1]
                if substring == substring[::-1]:
                    print(substring)

        print()

input_strings = ["racecar", "level", "hello"]
find_palindrom(input_strings)