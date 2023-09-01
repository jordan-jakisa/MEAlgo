def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return target
        elif nums[mid] < target:
            left  = mid + 1
        else:
            right = mid - 1
    return left

# Test cases
nums1 = [1, 3, 5, 6]
target1 = 5
print(searchInsert(nums1, target1))  # Output: 2

nums2 = [1, 3, 5, 6]
target2 = 2
print(searchInsert(nums2, target2))  # Output: 1

nums3 = [1, 3, 5, 6]
target3 = 7
print(searchInsert(nums3, target3))  # Output: 4
