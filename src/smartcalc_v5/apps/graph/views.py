from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np
import base64
import io


def graph_view(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')

        # Проверка, является ли expression строкой
        if not isinstance(expression, str):
            return render(request, 'graph.html', {'error': 'Invalid expression'})


        # Создание массива значений x
        x = np.linspace(-10, 10, 1000)

        # Вычисление значений функции
        try:
            y = eval(expression, {'x': x})
        except (NameError, SyntaxError):
            return render(request, 'graph.html', {'error': 'Invalid expression'})

        # Построение графика
        fig, ax = plt.subplots()
        ax.plot(x, y)

        # Отметка координатных осей
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)

        # Включение сетки с адаптивным шагом
        ax.grid(True, linewidth=0.3, linestyle='--')

        # Сохранение графика во временный буфер
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        graph_url = base64.b64encode(buffer.getvalue()).decode()

        return render(request, 'graph.html', {'graph_url': graph_url})

    return render(request, 'graph.html')