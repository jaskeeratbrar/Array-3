## T(C): O(n) # Two pointer approach.
## S(c): O(1)

## we will keep the highest position from left and right stationary, and move the shorter height pointer to either left or right

class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) < 1:
            return 0

        l, r = 0 , len(height) - 1

        maxL = height[l]
        maxR = height[r]

        result = 0    

        while(l < r):

          ## if height of right index is greater than the maximum we've seen on left

            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                result += maxL - height[l] 
              
          ## if height of left index is greater than the maximum we've seen on left, we shift our right pointer inward
  
            else:
                r -= 1
                maxR = max(maxR, height[r])
                result += maxR - height[r]

        return result
