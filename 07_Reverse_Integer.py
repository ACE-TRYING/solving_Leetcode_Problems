"""
Question=> 07:

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

"""

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse digits using string slicing
        reversed_x = int(str(x)[::-1]) * sign
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
    
        return reversed_x