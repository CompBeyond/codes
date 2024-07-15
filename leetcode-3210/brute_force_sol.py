class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        rt = ''
        for i in range(n):
            rt += s[(i + k) % n]
        return rt
