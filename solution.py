nums = [2,2,1,1,1,2,2,1,1,3,3,3,3,3,3,3,3,3]

def majorityElement(nums):
    counts = dict()
    for num in nums:
        # If num exists in counts, adding one to it, otherwise get() returns zero, a new key is created, and one is still added
        counts[num] = counts.get(num, 0) + 1
    # Max function returns the key with the largest value
    return max(counts)

print(majorityElement(nums))