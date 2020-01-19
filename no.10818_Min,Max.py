n = int(input())
num_list = list(map(int, input().split()))

min = num_list[0]
max = num_list[0]

for num in num_list:
    if num > max:
        max = num
    if num < min:
        min = num

print(min, max)