class Solution:
    def valid(self, s: str) -> bool:
        stack = []
        list = s.split(',')
        bracket_pairs = {'(': ')', '{': '}', '[': ']', '<': '>'}
        for elem in list:
            if elem in bracket_pairs:
                stack.append(elem)
            elif elem in bracket_pairs.values():
                if not stack or bracket_pairs[stack.pop()] != elem:
                    return False
        return not stack


s = Solution()
res = s.valid('(,),{,},[,<,<,>')
print(res)
