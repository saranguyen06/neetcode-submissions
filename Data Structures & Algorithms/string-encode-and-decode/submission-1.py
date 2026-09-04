class Solution:

    def encode(self, strs: List[str]) -> str:
        #prefix each string with its length and a special delimiter (like #) to completely avoid collision issues if the delimiter character appears inside the original text
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s))
            encoded_string += "#"
            encoded_string += s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded_strs.append(s[i:j])
            i = j

        return decoded_strs
