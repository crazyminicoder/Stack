class Solution:
    def baseBall(self, oper):
        stack = []
        sum = 0
        for i in oper:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            if i == 'C' and stack:
                stack.pop()
            if i == 'D' and stack:
                num = stack.pop()
                num2 = num * 2
                stack.append(num)
                stack.append(num2)
            if i == '+' and stack:
                num1 = stack.pop()
                if stack:
                    num2 = stack.pop()
                    res = num2 + num1
                    stack.append(num2)
                    stack.append(num1)
                    stack.append(res)
                else:
                    return 'Invalid operation',
        for i in stack:
            sum += i

        return sum


res = Solution()
# print(res.baseBall(['5', '2', 'C', 'D', '+']))

print(res.baseBall(['5', '-2', '4', 'C', 'D', '9', '+', '+']))
