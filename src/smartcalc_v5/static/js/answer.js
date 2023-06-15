<!DOCTYPE html>
<html>
<head>
    <title>Калькулятор</title>
    <style>
        .calculator {
            width: 200px;
            border: 1px solid #ccc;
            padding: 10px;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <input type="text" id="display" disabled>
        <br>
        <button onclick="addToDisplay('1')">1</button>
        <button onclick="addToDisplay('2')">2</button>
        <button onclick="addToDisplay('3')">3</button>
        <br>
        <button onclick="addToDisplay('4')">4</button>
        <button onclick="addToDisplay('5')">5</button>
        <button onclick="addToDisplay('6')">6</button>
        <br>
        <button onclick="addToDisplay('7')">7</button>
        <button onclick="addToDisplay('8')">8</button>
        <button onclick="addToDisplay('9')">9</button>
        <br>
        <button onclick="addToDisplay('0')">0</button>
        <button onclick="addToDisplay('.')">.</button>
        <br>
        <button onclick="clearDisplay()">Clear</button>
        <button onclick="calculate()">Calculate</button>
    </div>

    <script>
        function addToDisplay(value) {
            document.getElementById('display').value += value;
        }

        function clearDisplay() {
            document.getElementById('display').value = '';
        }

        function calculate() {
            var displayValue = document.getElementById('display').value;
            var result = eval(displayValue); // Используем eval для вычисления строки с математическим выражением

            document.getElementById('display').value = result;
        }
    </script>
</body>
</html>
