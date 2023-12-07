def twoSum(nums, target):
    num_map = {}  # Create an empty hash map
    for i, num in enumerate(nums):  # Iterate over the numbers with their indices
        complement = target - num  # Calculate the complement
        if complement in num_map:  # If the complement is in the map, we found a pair
            return [num_map[complement], i]  # Return the indices
        num_map[num] = i  # Add the number and its index to the map
    return []  # Return an empty list if no pair is found
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
