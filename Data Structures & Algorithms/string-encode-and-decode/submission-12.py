class Solution:
    
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ''
        for s in strs:
            encoded += f'#{len(s)}${s}'
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        res = []
        while i < len(s):
            if s[i] == '#':
                length = ''
                i += 1
                while s[i] in '0123456789':
                    length += s[i]
                    i += 1
                i += 1
            res.append(s[i:i+int(length)])
            i = i + int(length)
        return res