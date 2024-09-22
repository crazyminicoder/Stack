# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

class Solution:
    def backSpace(self, s, t):
        stack1 = []
        stack2 = []
        for i in s:
            if i != '#':
                stack1.append(i)
            else:
                if stack1 and i == '#':
                    stack1.pop()

        for j in t:
            if j != '#':
                stack2.append(j)
            else:
                if stack2 and j == '#':
                    stack2.pop()

        str1 = ''.join(stack1)
        str2 = ''.join(stack2)

        if str1 == str2:
            return True
        else:
            return False


res = Solution()
print(res.backSpace("ab#c", "d##"))
