class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        digit_idx = 0
        pairs = [['I', 'V'], ['X', 'L'], ['C', 'D'], ['M', 'N/A']]
        while num:
            digit = num % 10
            num = int(num / 10)
            current_pair = pairs[digit_idx]
            next_pair = pairs[digit_idx+1] if digit_idx+1 < len(pairs) else None
            digit_idx += 1
            if digit == 0:
                pass
            elif digit <= 3:
                for _ in range(digit):
                    res = current_pair[0] + res
            elif digit == 4:
                res = current_pair[0] + current_pair[1] + res
            elif digit == 5:
                res = current_pair[1] + res
            elif digit <= 8:
                for _ in range(digit-5):
                    res = current_pair[0] + res
                res = current_pair[1] + res
            elif digit == 9:
                res = current_pair[0] + next_pair[0] + res
                
        return res
