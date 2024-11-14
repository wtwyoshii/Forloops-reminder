#Write a program that uses nested for loops to 
# find and print all pairs of numbers from a list 
# that add up to a specific target sum. For example, 
# given [1, 2, 3, 4, 5] and target sum 5, it should print (1, 4) and (2, 3).

def find_pairs(nums, sum):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == sum:
                print(f"({nums[i]}, {nums[j]})")
nums = [9, 11, 12, 8, 3, 2, 4]
sum = 20
find_pairs(nums, sum)
