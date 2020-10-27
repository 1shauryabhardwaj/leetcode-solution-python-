
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long = 0
        a1 = []
        if s == "":
            return 0
        else:
            for i in s:
                if i in a1:
                    if long < len(a1):
                        long = len(a1)
                    a1 = a1[a1.index(i)+1::]
                a1.append(i)
        return max(len(a1),long)