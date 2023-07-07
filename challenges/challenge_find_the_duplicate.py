def find_duplicate(nums):
    if len(nums) <= 1:
        return False
    nums.sort()
    for i, n in enumerate(nums):
        if isinstance(n, str) or n < 1:
            return False
        if i < len(nums) - 1 and n == nums[i + 1]:
            return n
    return False
