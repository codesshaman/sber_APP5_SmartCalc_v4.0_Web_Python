import math
import re


def parse_expression(expression):
    # Используем регулярное выражение для разделения строки на числа, операции и скобки
    tokens = re.findall(r'[\d.]+|\+|\-|\*|/|\(|\)', expression)

    # Создаём пустой стек
    stack = []

    # Создаём пустой список для хранения чисел и операций
    output = []

    # Определяем приоритеты операций
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    # Обрабатываем каждый токен в выражении
    for token in tokens:
        if token.isdigit() or '.' in token:
            # Если токен является числом, добавляем его в выходной список
            output.append(float(token))
        elif token in ('+', '-', '*', '/'):
            # Если токен является операцией
            while stack and stack[-1] != '(' and precedence[token] <= precedence.get(stack[-1], 0):
                # Проверяем приоритет текущей операции относительно операций в стеке
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            # Если токен является открывающей скобкой, добавляем его в стек
            stack.append(token)
        elif token == ')':
            # Если токен является закрывающей скобкой
            while stack and stack[-1] != '(':
                # Перемещаем операции из стека в выходной список, пока не встретим открывающую скобку
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                # Удаляем открывающую скобку из стека
                stack.pop()

    # Добавляем оставшиеся операции из стека в выходной список
    while stack:
        output.append(stack.pop())

    return output


def evaluate_expression(tokens):
    stack = []

    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in ('+', '-', '*', '/'):
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            stack.append(result)

    return stack.pop()