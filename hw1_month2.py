class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Ошибка: деление на ноль"

def main():
    calculator = Calculator()

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    choice = input("Введите номер операции (1 /2 /3 /4 ): ")

    if choice in ['1', '2', '3', '4']:
        if choice == '1':
            result = calculator.add(num1, num2)
            print(f"Результат сложения: {result}")
        elif choice == '2':
            result = calculator.subtract(num1, num2)
            print(f"Результат вычитания: {result}")
        elif choice == '3':
            result = calculator.multiply(num1, num2)
            print(f"Результат умножения: {result}")
        elif choice == '4':
            result = calculator.divide(num1, num2)
            print(f"Результат деления: {result}")
    else:
        print("Неверный выбор операции")

if __name__ == "__main__":
    main()
