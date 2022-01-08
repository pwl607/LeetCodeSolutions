from typing import List
import  collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for x in strs :
            key = ''.join(sorted(x))    #sorted(字符串)会返回一个按ascii排序的列表
            mp[key].append(x)           #以排序后的字符串为key，添加当前字符串

        return list(mp.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))