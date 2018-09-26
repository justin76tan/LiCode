'''

There is a special square room with mirrors on each of the four walls.
Except for the southwest corner,
there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p,
and a laser ray from the southwest corner first meets the east wall
at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.
(It is guaranteed that the ray will meet a receptor eventually.)



Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.



Note:

1 <= p <= 1000
0 <= q <= p

'''


class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        k = 1
        while p*k % q != 0:
            k += 1

        if k % 2 == 0: return 0
        else:

            r = p*k / q
            if r % 2 == 1: return 1
            if r % 2 == 0: return 2

p = 4
q = 3

s = Solution()
print(s.mirrorReflection(p, q))



