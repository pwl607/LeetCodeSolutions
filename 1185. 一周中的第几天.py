'''输入日期year, month, day判断是星期几'''
'''用塞勒公式，注意调整1月和2月，视为前一年的13月和14月'''
'''公式算出结果0表示星期六，1表示星期日……6表示星期五'''

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        if month < 3 :
            month += 12
            year -= 1
        return ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday'][(day + 13 * (month + 1) // 5 + year + year // 4 - year // 100 + year // 400) % 7]

day = 7
month = 6
year = 1990
print(Solution().dayOfTheWeek(day, month, year))