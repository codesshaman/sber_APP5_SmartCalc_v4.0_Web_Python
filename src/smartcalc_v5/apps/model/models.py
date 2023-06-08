from django.http import HttpResponse
import math


# Create your models here.
def process(request):
    input_value = request.GET.get('input', '')
    try:
        result = 'Результат=' + input  # eval(input_value)
        return HttpResponse(str(result))
    except:
        return HttpResponse("Error: Invalid input")


def math_pi():
    return math.pi


def math_e():
    return math.e


def zero_killer(value):
    string = str(value)
    num = string.split(".")
    if num[1] == "0":
        return int(num[0])
    else:
        return value


class SmartCalc():
    """Основной класс модели"""

    def __init__(self, number):
        self.value = number

    def dot_find(self):
        return self.value.find(".")

    def types_convert(self):
        if self.dot_find() == -1:
            return int(self.value)
        else:
            return float(self.value)

    def math_eval(self):
        if len(str(self.value)) > 0:
            return eval(value)
        else:
            return 0

    def math_ln(self):
        try:
            return math.log(self.types_convert())
        except:
            return 0

    def math_log(self):
        try:
            return math.log10(self.types_convert())
        except:
            return 0

    def math_sin(self):
        try:
            return math.sin(self.types_convert())
        except:
            return 0

    def math_asin(self):
        try:
            return math.asin(self.types_convert())
        except:
            return 0

    def math_cos(self):
        try:
            return math.cos(self.types_convert())
        except:
            return 0

    def math_acos(self):
        try:
            return math.acos(self.types_convert())
        except:
            return 0

    def math_tan(self):
        try:
            return math.tan(self.types_convert())
        except:
            return 0

    def math_atan(self):
        try:
            return math.atan(self.types_convert())
        except:
            return 0

    def math_sqrt(self):
        res = math.sqrt(self.types_convert())
        return zero_killer(res)

    def math_power(self):
        res = math.pow(self.types_convert(), 2)
        return zero_killer(res)


value = '-1.8'


def main():
    calc = SmartCalc(value)
    res = calc.math_log()
    print(type(res))
    print(res)


if __name__ == '__main__':
    main()
