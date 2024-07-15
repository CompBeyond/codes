class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        invert_point = k % len(s)
        return s[invert_point:] + s[:invert_point]
