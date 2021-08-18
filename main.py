# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/5_Stack/5_stack_exercise.md
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        if len(self.container) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.container)

    def print_stack(self):
        for item in self.container:
            print(item)


def is_balanced(val):
    s = Stack()
    balanced = True
    for ch in str(val):
        if ch == "(" or ch == "{" or ch == "[":
            s.push(ch)
        elif ch == ")" or ch == "}" or ch == "]":
            if s.is_empty():
                balanced = False
                break
            else:
                s.pop()

    if s.is_empty() and balanced:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_balanced("({a+b})"))  # True
    print(is_balanced("))((a+b}{"))  # False
    print(is_balanced("((a+b))"))  # True
    print(is_balanced("))"))  # False
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))  # True
