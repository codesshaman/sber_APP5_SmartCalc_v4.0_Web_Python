import re
from core import SmartCalc as sc

def parse_expression(expression):
    # Используем регулярное выражение для разделения строки на числа, операции и скобки
    pattern = r"(\s*sin\s+" \
              r"|\s*cos\s+" \
              r"|\s*acos\s+" \
              r"|\s*asin\s+" \
              r"|\s*ln\s+" \
              r"|\s*log\s+" \
              r"|\s*tan\s+" \
              r"|\s*atan\s+" \
              r"|\s*sqrt\s+" \
              r"|[\d.]+|\+|\-|\*|/|\(|\))"
    tokens = re.findall(pattern, expression)

    # Формируем словарь токенов
    dict = ('+', '-', '*', '/',
            'sin ', 'cos ', 'acos ', 'asin ',
            'ln ', 'log ', 'tan ', 'atan ', 'sqrt ')
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
        elif token.strip() in dict:
            # Если токен является операцией
            while stack and stack[-1] != '(' and precedence[token] <= precedence.get(stack[-1], 0):
                # Проверяем приоритет текущей операции относительно операций в стеке
                output.append(stack.pop())
            stack.append(token.strip())
        elif token in dict:
            # Если токен есть в словаре токенов, добавляем его в стек
            stack.append(token.strip())
        elif token == '(':
            # Если токен является открывающей скобкой, добавляем его в стек
            stack.append(token.strip())
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
    dict = ('+', '-', '*', '/',
            'sin ', 'cos ', 'acos ', 'asin ',
            'ln ', 'log ', 'tan ', 'atan ', 'sqrt ')

    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in dict:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '-':
                result = operand1 - operand2
            elif token == '+':
                result = operand1 + operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            elif token == 'cos':
                result = sc.math_cos(operand1)
            elif token == 'sin':
                result = operand1 / operand2
            elif token == 'acos':
                result = operand1 / operand2
            elif token == 'asin':
                result = operand1 / operand2
            elif token == 'ln':
                result = operand1 / operand2
            elif token == 'log':
                result = operand1 / operand2
            elif token == 'tan':
                result = operand1 / operand2
            elif token == 'atan':
                result = operand1 / operand2
            elif token == 'sqrt':
                result = operand1 / operand2
            stack.append(result)

    return stack.pop()


# def result_display(value):
#     string = str(value)
#     num = string.split(".")
#     if num[1] == "0":
#         return int(num[0])
#     else:
#         return value

def main():
    expression = "cos 0.333"
    parsed_tokens = parse_expression(expression)
    result = evaluate_expression(parsed_tokens)
    # result = result_display(result)
    print(result)


if __name__ == '__main__':
    main()
