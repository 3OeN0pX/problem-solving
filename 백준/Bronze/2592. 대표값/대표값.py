nums = [int(input()) for _ in range(10)]

print(sum(nums) // 10)

count = {}
for num in nums:
    count[num] = count.get(num, 0) + 1

mode = max(count, key=count.get)
print(mode)