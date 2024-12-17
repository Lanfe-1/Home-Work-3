nums = []
if len(nums) > 0:
    nums.insert(0, nums[-1])
    nums.pop()
print(nums)

nums = [1, 2, 3]
middle_index = len(nums)// 2

if len(nums) % 2 != 0:
    middle_index += 1

part1 = nums[:middle_index]
part2 = nums[middle_index: ]
result = [part1 , part2]

print(result)
