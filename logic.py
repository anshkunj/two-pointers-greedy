"""
logic.py
Two Pointers & Greedy problem solutions
"""

from typing import List

# 1️⃣ Container With Most Water
def max_area(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    max_a = 0
    while l < r:
        max_a = max(max_a, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_a

# 2️⃣ 3Sum
def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, n-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res

# 3️⃣ 3Sum Closest
def three_sum_closest(nums: List[int], target: int) -> int:
    nums.sort()
    closest = float('inf')
    n = len(nums)
    for i in range(n):
        l, r = i+1, n-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if abs(s - target) < abs(closest - target):
                closest = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return target
    return closest

# 4️⃣ Two Sum II - Input array sorted
def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        else:
            r -= 1
    return []

# 5️⃣ Remove Duplicates from Sorted Array
def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    l = 0
    for r in range(1, len(nums)):
        if nums[r] != nums[l]:
            l += 1
            nums[l] = nums[r]
    return l + 1

# 6️⃣ Squares of a Sorted Array
def sorted_squares(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n
    l, r = 0, n-1
    pos = n-1
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            result[pos] = nums[l]**2
            l += 1
        else:
            result[pos] = nums[r]**2
            r -= 1
        pos -= 1
    return result

# 7️⃣ Merge Sorted Array
def merge_sorted(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1, p2, p = m-1, n-1, m+n-1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

# 8️⃣ Intersection of Two Arrays II
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    l, r = 0, 0
    res = []
    while l < len(nums1) and r < len(nums2):
        if nums1[l] == nums2[r]:
            res.append(nums1[l])
            l += 1
            r += 1
        elif nums1[l] < nums2[r]:
            l += 1
        else:
            r += 1
    return res

# 9️⃣ Remove Element
def remove_element(nums: List[int], val: int) -> int:
    l = 0
    for r in range(len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1
    return l

# 1️⃣0️⃣ Valid Palindrome
def valid_palindrome(s: str) -> bool:
    def is_pal(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return is_pal(l+1, r) or is_pal(l, r-1)
        l += 1
        r -= 1
    return True

# 1️⃣1️⃣ Longest Mountain in Array
def longest_mountain(arr: List[int]) -> int:
    n = len(arr)
    max_len = 0
    i = 1
    while i < n-1:
        if arr[i-1] < arr[i] > arr[i+1]:
            l, r = i-1, i+1
            while l > 0 and arr[l-1] < arr[l]:
                l -= 1
            while r < n-1 and arr[r] > arr[r+1]:
                r += 1
            max_len = max(max_len, r - l + 1)
            i = r
        else:
            i += 1
    return max_len

# 1️⃣2️⃣ Candy (Greedy)
def candy(ratings: List[int]) -> int:
    n = len(ratings)
    left = [1] * n
    right = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            left[i] = left[i-1] + 1
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            right[i] = right[i+1] + 1
    return sum(max(left[i], right[i]) for i in range(n))