"""判断两个字符串是否同构。同构的定义是，可以通过把一个字符串的某些相同的字符转换成
另一些相同的字符，使得两个字符串相同，且两种不同的字符不能够被转换成同一种字符。"""


"""
核心思路

使用两个哈希表（字典）分别记录两个字符串中字符的映射关系：
正向映射：s中的字符映射到 t中的字符。
反向映射：t中的字符映射到 s中的字符。
算法步骤
长度检查：如果两个字符串长度不同，直接返回 False。
遍历字符：同时遍历两个字符串的每个字符 char_s和 char_t。
检查正向映射：
如果 char_s已经存在于正向映射中，检查它映射的值是否等于当前的 char_t。
如果不相等，说明 char_s试图映射到两个不同的字符，返回 False。
检查反向映射：
如果 char_t已经存在于反向映射中，检查它映射的值是否等于当前的 char_s。
如果不相等，说明 char_t被两个不同的字符映射，返回 False。
建立映射：如果上述检查都通过，则建立双向映射。
返回结果：遍历结束后，说明所有字符都满足同构条件，返回 True。

"""

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # 建立双向映射表
    s_to_t = {}  # 记录 s 中字符映射到 t 中哪个字符
    t_to_s = {}  # 记录 t 中字符被 s 中哪个字符映射

    for char_s, char_t in zip(s, t):
        # 检查正向映射：s 中的字符是否映射到正确的 t 字符
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        # 检查反向映射：t 中的字符是否被正确的 s 字符映射
        elif char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            # 建立双向映射
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

    return True
