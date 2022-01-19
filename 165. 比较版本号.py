class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vs1 = [int(x) for x in version1.split('.')]
        vs2 = [int(x) for x in version2.split('.')]
        while len(vs1) < len(vs2):
            vs1 = vs1 + [0]
        while len(vs1) > len(vs2):
            vs2 = vs2 + [0]
        for i in range(len(vs1)):
            if vs1[i] > vs2[i]:
                return 1
            if vs1[i] < vs2[i]:
                return -1
        return 0



version1 = "1.0.1"
version2 = "1.0.1.0.0.0.0"
print(Solution().compareVersion(version1, version2))