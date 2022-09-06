#258. 各位相加
#https://leetcode.cn/problems/add-digits/

def addDigits(num):

    while num >= 10:
        sum=0
        while num:
            sum += num % 10
            num  //= 10
        num=sum
    return num

print(addDigits(3814))
