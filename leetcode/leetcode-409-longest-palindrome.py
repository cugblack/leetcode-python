# 409. 最长回文串
# https://leetcode-cn.com/problems/longest-palindrome/


def longest_palindrome(s: str) -> int:
    """
    input:
        s: str
    output：
        length: 最长回文串
    思路：
        1) 统计所有字符串出现的次数
        2）求和：偶数次的出现次数+ （奇数次-1）
        3） 加1，只使用一次技术
    """
    from collections import Counter
    d = Counter(s)
    ans = 0
    for i in d.values():
        ans += i // 2 * 2
        if ans % 2 == 0 and i % 2 == 1:
            ans += 1
    return ans


if __name__ == "__main__":
    s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    print(longest_palindrome(s))
