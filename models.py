"""
models.py
Pydantic models for Two Pointers & Greedy API
"""

from pydantic import BaseModel
from typing import List

# Generic List[int] + target (two sum, mountain, etc.)
class ArrayInput(BaseModel):
    nums: List[int]

class ArrayTwoInput(BaseModel):
    nums1: List[int]
    nums2: List[int]

class ArrayTargetInput(BaseModel):
    nums: List[int]
    target: int

class ArrayValInput(BaseModel):
    nums: List[int]
    val: int

# String input for palindrome
class StringInput(BaseModel):
    s: str

# Ratings for candy problem
class RatingsInput(BaseModel):
    ratings: List[int]