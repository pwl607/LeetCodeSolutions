'''给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vis = set()
        left, right, ans = 0, 0, 0
        while right < len(s) :
            if s[right] in vis :
                while s[right] in vis :
                    vis.remove(s[left])
                    left += 1
            vis.add(s[right])
            ans = max(right - left + 1, ans)
            print(s[left:right+1])
            right += 1
        return ans
        


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))