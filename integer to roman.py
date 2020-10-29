class Solution:
    def intToRoman(self, num: int) -> str:
        accum = num
        thousands = accum // 1000
        accum %= 1000
        
        fivehundreds = accum // 500
        accum %= 500
        
        hundreds = accum // 100
        accum %= 100
        
        fifties = accum // 50
        accum %= 50
        
        tens = accum // 10
        accum %= 10
        
        fives = accum // 5
        accum %= 5
        
        ones = accum
        
        numstr = thousands*"M"+fivehundreds*"D"+hundreds*"C"+fifties*"L"+tens*"X"+fives*"V"+ones*"I"
        numstr = numstr.replace("DCCCC", "CM").replace("CCCC", "CD")
        numstr = numstr.replace("LXXXX", "XC").replace("XXXX", "XL").replace("VIIII", "IX").replace("IIII", "IV")
        return numstr