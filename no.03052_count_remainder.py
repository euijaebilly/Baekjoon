num_list = []
remainder_list = []

for i in range(10):
    num_list.append(int(input()))
    remainder_list.append(num_list[i] % 42)

remainder_list = list(set(remainder_list))

print(len(remainder_list))