class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for digit in digits:
            string += str(digit)
        integer = int(string) + 1
        stringInt = str(integer)
        digits = []
        for i in range(0, len(str(integer))):
            digits.append(stringInt[i])
        return digits
