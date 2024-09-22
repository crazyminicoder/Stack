# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

class Solution:
    def nextGreaterElement(self, num1, num2):
        stack = []
        dict = {}
        for i in reversed(num2):
            while stack and stack[-1] <= i:
                stack.pop()

            if stack:
                dict[i] = stack[-1]
            else:
                dict[i] = -1

            stack.append(i)

        return [dict[i] for i in num1]


num1 = [4, 1, 2]
num2 = [1, 3, 4, 2]
res = Solution()
print(res.nextGreaterElement(num1, num2))
