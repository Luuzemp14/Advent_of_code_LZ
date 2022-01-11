#Part 1
"""
with open("input_aoc_1") as f:
    lines = f.readlines()
    nums = [int(line.strip()) for line in lines]
    for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
            num1 = nums[i]
            num2 = nums[j]

            if num1 + num2 == 2020:
                balance = num1 * num2

    print(balance)
"""
#Part 2

with open("input_aoc_1") as f:
    lines = f.readlines()
    nums = [int(line.strip()) for line in lines]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                num1 = nums[i]
                num2 = nums[j]
                num3 = nums[k]

                if num1 + num2 + num3 == 2020:
                    balance = num1 * num2 * num3
print(balance)
