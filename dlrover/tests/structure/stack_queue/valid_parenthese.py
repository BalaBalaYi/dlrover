"""给定一个只由左右原括号、花括号和方括号组成的字符串，求这个字符串是否合法。合法的
定义是每一个类型的左括号都有一个右括号一一对应，且括号内的字符串也满足此要求。"""


def is_valid(s: str) -> bool:
    mapping = {")":"(", "]":"[", "}":"{"}
    stack = []

    for char in s:
        if char in mapping:
            # 如果是右括号
            value = stack.pop() if stack else None
            if value and mapping[char] != value:
                return False
        else:
            # 如果是左括号
            stack.append(char)

    return not stack
