def is_balanced(expression):
    stack = []
    for character in expression:
        if character in '([{':
           stack.append(character)
        elif character in ')]}':
            if not stack:
                return False
            added = stack.pop()
            if added == '(' and character != ')' or added == '[' and character != ']' or added == '{' and character != '}':
                return False
    return not stack

            
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1)) 
print(is_balanced(expression2))
