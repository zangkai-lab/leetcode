from typing import List
import collections

'''
@time: 10月11日
@question: 273. 整数转换英文表示
@analysis: 
    # 2的31的次方是2 147 483 648 一共10位
    # 使用字典，三位一循环，怎么得到字符串的输出
'''

singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        def recursion(num:int) -> str:
            s = ''
            if num == 0:
                return s
            elif num < 10:
                s += singles[num] + ' '
            elif num < 20:
                s += teens[num-10] + ' '
            elif num < 100:
                s += tens[num//10] + ' ' + recursion(num % 10)
            else:
                s += singles[num // 100] + 'Hundred' + recursion(num % 100)
            return s
        s = ''
        unit = int(1e9)
        for i in range(3,-1,-1):
            curNum = num // unit
            if curNum:
                num -= curNum * unit
                s += recursion(curNum) + thousands[i] + ' '
            unit //= 1000
        return s.strip()



