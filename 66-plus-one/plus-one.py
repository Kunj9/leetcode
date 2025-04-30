class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(map(str, digits)))
        total = number+1
        digits = [int(d) for d in str(total)]
        return digits 