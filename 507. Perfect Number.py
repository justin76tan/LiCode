'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
'''


class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = 1
        result = 0

        while n * n <= num:
            if num % n == 0:
                result += n

                if n * n != num:
                    result += num // n

            n += 1

        return result-num == num


s = Solution()
num = 28
print(s.checkPerfectNumber(num))