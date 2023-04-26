nums = [3,3,4]

def majorityElement(nums):
    counts = dict()
    for num in nums:
        # If num exists in counts, adding one to it, otherwise get() returns zero, a new key is created, and one is still added
        counts[num] = counts.get(num, 0) + 1
    # Max function returns the key with the largest value
    # Need to use the key parameter in max() to get the dictionary key with the largest value (key=counts.get)
    # Found: https://datagy.io/python-get-dictionary-key-with-max-value/
    return max(counts, key=counts.get)

print(majorityElement(nums))