class Solution(object):
    @staticmethod
    def title_to_number(s):
        return sum(26**p*(ord(c)-64) for p, c in enumerate(s[::-1]))

print(Solution.title_to_number('AA'))
