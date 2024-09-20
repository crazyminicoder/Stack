class Solution:
    def smallestNumber(self, num, k) -> int:
        stack = []
        for i in num:
            while k > 0 and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)

        while k > 0:
            stack.pop()
            k -= 1

        result = ''.join(stack).lstrip('0')

        return result if result else "0"


s = Solution()
print(s.smallestNumber("1432219", 3))
