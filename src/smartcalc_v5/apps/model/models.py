from django.http import HttpResponse
from . import mathfunc
from urllib.parse import parse_qs


# Create your models here.
def result_display(value):
    string = str(value)
    num = string.split(".")
    if num[1] == "0":
        return int(num[0])
    else:
        return value


def main():
    expression = "(3 + 4)"
    parsed_tokens = mathfunc.parse_expression(expression)
    result = mathfunc.evaluate_expression(parsed_tokens)
    print(result)


if __name__ == '__main__':
    main()


def process(request):
    expression = request.GET.get('input', '')
    # parsed = parse_qs(expression)
    # expression = parsed.get('expression', [''])[0]
    try:
        parsed_tokens = mathfunc.parse_expression(expression)
        result = mathfunc.evaluate_expression(parsed_tokens)
        result = result_display(result)
        return HttpResponse(str(result))
    except:
        return HttpResponse("0")
