from operator import add, mul, sub
from operator import truediv as div
from typing import List


def prefix_evaluate(prefix_evaluation: List[str]) -> int:
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    queue = prefix_evaluation
    stack = []
    for i in queue:
        if i in ["+", "-", "*", "/"]:
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(ops[i](b, a))
        else:
            stack.append(i)
    return stack[-1]


def to_prefix(equation: str) -> List[str]:
    stack = []
    queue = []
    equation = equation.split()
    priority = {"+": 0, "-": 0, "*": 1, "/": 1}
    for i in equation:
        if i in ["+", "-", "*", "/"]:
            if len(stack) == 0 or stack[-1] =='(':
                stack.append(i)
            elif priority[i] > priority[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 0 and stack[-1] != '(' and priority[i] <= priority[stack[-1]]:
                    queue.append(stack.pop())
                stack.append(i)
        elif i == "(":
            stack.append(i)
        elif i == ")":
            while stack[-1] != "(":
                queue.append(stack.pop())
            stack.pop() 
        else:
            queue.append(int(i))
    while  len(stack) > 0:
        queue.append(stack.pop())
    return queue


def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))
