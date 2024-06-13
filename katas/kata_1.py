def bracket_matcher(string: str) -> bool:
    stack = []
    bracket_pairs = {")":"(", "]":"[", "}":"{"}

    for char in string:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            if stack[-1] == bracket_pairs[char]:
                stack.pop()
            else:
                return False
 
    return len(stack) == 0
