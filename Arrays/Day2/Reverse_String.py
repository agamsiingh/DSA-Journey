class Solution(object):
    def reverseString(self, s):
        left, right = 0, len(s) - 1  # 1️⃣ initialize two pointers

        while left < right:         # 2️⃣ loop until the pointers meet
            s[left], s[right] = s[right], s[left]  # 3️⃣ swap the characters
            left += 1               # 4️⃣ move left pointer to the right
            right -= 1              # 5️⃣ move right pointer to the left