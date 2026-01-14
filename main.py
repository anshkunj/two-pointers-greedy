"""
main.py
FastAPI app for Two Pointers & Greedy Repo
All 12 problems exposed as API endpoints
"""

from fastapi import FastAPI
from logic import *
from models import *

app = FastAPI(title="Two Pointers & Greedy API")

@app.get("/")
def root():
    return {"message": "Welcome to Two Pointers & Greedy API!"}

# 1️⃣ Container With Most Water
@app.post("/container_with_most_water")
def api_max_area_post(input: ArrayInput):
    return {"result": max_area(input.nums)}

@app.get("/container_with_most_water")
def api_max_area_get(nums: str):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": max_area(nums_list)}


# 2️⃣ 3Sum
@app.post("/three_sum")
def api_three_sum_post(input: ArrayInput):
    return {"result": three_sum(input.nums)}

@app.get("/three_sum")
def api_three_sum_get(nums: str):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": three_sum(nums_list)}


# 3️⃣ 3Sum Closest
@app.post("/three_sum_closest")
def api_three_sum_closest_post(input: ArrayTargetInput):
    return {"result": three_sum_closest(input.nums, input.target)}

@app.get("/three_sum_closest")
def api_three_sum_closest_get(nums: str, target: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": three_sum_closest(nums_list, target)}


# 4️⃣ Two Sum II - Input array sorted
@app.post("/two_sum_sorted")
def api_two_sum_post(input: ArrayTargetInput):
    return {"result": two_sum_sorted(input.nums, input.target)}

@app.get("/two_sum_sorted")
def api_two_sum_get(nums: str, target: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": two_sum_sorted(nums_list, target)}


# 5️⃣ Remove Duplicates from Sorted Array
@app.post("/remove_duplicates")
def api_remove_duplicates_post(input: ArrayInput):
    return {"result": remove_duplicates(input.nums)}

@app.get("/remove_duplicates")
def api_remove_duplicates_get(nums: str):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": remove_duplicates(nums_list)}


# 6️⃣ Squares of a Sorted Array
@app.post("/sorted_squares")
def api_sorted_squares_post(input: ArrayInput):
    return {"result": sorted_squares(input.nums)}

@app.get("/sorted_squares")
def api_sorted_squares_get(nums: str):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": sorted_squares(nums_list)}


# 7️⃣ Merge Sorted Array
@app.post("/merge_sorted")
def api_merge_sorted_post(input: ArrayTwoInput):
    nums1 = input.nums1
    nums2 = input.nums2
    merge_sorted(nums1, len(nums1), nums2, len(nums2))
    return {"result": nums1}

@app.get("/merge_sorted")
def api_merge_sorted_get(nums1: str, nums2: str):
    nums1_list = [int(x) for x in nums1.split(",")]
    nums2_list = [int(x) for x in nums2.split(",")]
    merge_sorted(nums1_list, len(nums1_list), nums2_list, len(nums2_list))
    return {"result": nums1_list}


# 8️⃣ Intersection of Two Arrays II
@app.post("/intersect_arrays")
def api_intersect_post(input: ArrayTwoInput):
    return {"result": intersect(input.nums1, input.nums2)}

@app.get("/intersect_arrays")
def api_intersect_get(nums1: str, nums2: str):
    nums1_list = [int(x) for x in nums1.split(",")]
    nums2_list = [int(x) for x in nums2.split(",")]
    return {"result": intersect(nums1_list, nums2_list)}


# 9️⃣ Remove Element
@app.post("/remove_element")
def api_remove_element_post(input: ArrayValInput):
    return {"result": remove_element(input.nums, input.val)}

@app.get("/remove_element")
def api_remove_element_get(nums: str, val: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": remove_element(nums_list, val)}


# 1️⃣0️⃣ Valid Palindrome
@app.post("/valid_palindrome")
def api_valid_palindrome_post(input: StringInput):
    return {"result": valid_palindrome(input.s)}

@app.get("/valid_palindrome")
def api_valid_palindrome_get(s: str):
    return {"result": valid_palindrome(s)}


# 1️⃣1️⃣ Longest Mountain in Array
@app.post("/longest_mountain")
def api_longest_mountain_post(input: ArrayInput):
    return {"result": longest_mountain(input.nums)}

@app.get("/longest_mountain")
def api_longest_mountain_get(nums: str):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": longest_mountain(nums_list)}


# 1️⃣2️⃣ Candy (Greedy)
@app.post("/candy")
def api_candy_post(input: RatingsInput):
    return {"result": candy(input.ratings)}

@app.get("/candy")
def api_candy_get(ratings: str):
    ratings_list = [int(x) for x in ratings.split(",")]
    return {"result": candy(ratings_list)}