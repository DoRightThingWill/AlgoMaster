# Leetcode link: https://leetcode.com/problems/remove-k-digits/description/

# TODO:
# 1, if the digits are in ascending order, the number is min
# 2, if a smaller number is found, move to front and keep the ascending order, the number is min
# overall, it is greedy method. Here, we use monotonic stack to keep the ascending order of the digits

# TODO: syntax note
# 1, or operator in python, like return a or b. If a statement is truthy, return a. But if a is falsy, return b.
# 2, lstrip() in python is operation of string, to remove substring from the left end, or leading prefix. Like str = "abc", str.lstrip("a") return "bc"
# 3, rstrip() remove suffix from the right end
# 4, by default, if no substring provided into strip(), it removes white spaces from both sides. While lstrip() remove white space from left end; rstrip() remove white space from the right end.
# 5, string slice: s[:-k]. How does this work? [from:to:step]. Here, [:-k] means, keep substring from index = 0, to (not including) index = -k. This literally remove the last k letters from the right end.
# 6, similarly, if you want to remove the first k letter, you can use [k:]. Basically, [start:end] means keeping which part.


def get_min_number(num: str, k: int) -> str:
    stack = []

    for i, digit in enumerate(num):
        print(digit)
        while k and stack and num[stack[-1]] > int(digit):
            k -= 1
            stack.pop()
        stack.append(i)

    # case 1: digits in original num already in asc ordering, final stack holds all digits in num, then we simply trunk the num string by the last k digits
    # case 2: digits in original num not in asc order, some digits in the num are removed. Digits in the final stack forms the min final number

    if k == 0:
        # means there are some digits removed from the original num string. Now, the stack holds digits that form the min number.
        return "".join(stack).lstrip("0")
    else:
        # means we can further remove digits from num until it reach 0, and the digits in the final stack are in asc order
        return "".join(stack[:-k]) if k < len(stack) else "0"

num = "1432219"
get_min_number(num, 3)