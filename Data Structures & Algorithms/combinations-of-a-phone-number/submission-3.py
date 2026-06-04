class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }

        if not digits:
            return []

        res = []
        def combination(index, subset):
            if len(subset) == len(digits):
                res.append("".join(subset.copy()))
                return
            
            curr_digit_letters = mapping[digits[index]]
            for i in range(len(curr_digit_letters)):
                subset.append(curr_digit_letters[i])
                combination(index + 1, subset)
                subset.pop()
            
            return res
        return combination(0, [])
