num = 1

for i in range(3):
    num *= int(input())

nums = list(str(num))

result = []
for i in range(10):
    result.append(nums.count(str(i)))
    print(result[i])