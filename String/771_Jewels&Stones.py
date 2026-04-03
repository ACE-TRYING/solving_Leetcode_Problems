"""
Question=>771:

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num_jewels=0
        for s in stones:
            if s in jewels:
                num_jewels+=1
        return num_jewels    