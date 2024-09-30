import math

def main():
    while True:
        print("\nПростая калькуляторная программа")
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: Введите корректные числа!")
            continue

        print("\nВыберите операцию:")
        print("1: Сложение")
        print("2: Вычитание")
        print("3: Умножение")
        print("4: Деление")
        print("5: Возведение в степень")
        print("6: Извлечение квадратного корня (из первого числа)")
        print("7: Остаток от деления")
        print("8: Деление нацело")
        print("9: Синус (для первого числа)")
        print("10: Косинус (для первого числа)")
        print("0: Выход")

        choice = input("Введите номер операции: ")

        if choice == '1':
            print(f"Результат: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Результат: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Результат: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("Ошибка: Деление на ноль невозможно!")
            else:
                print(f"Результат: {num1} / {num2} = {num1 / num2}")
        elif choice == '5':
            print(f"Результат: {num1} ^ {num2} = {num1 ** num2}")
        elif choice == '6':
            if num1 < 0:
                print("Ошибка: Невозможно извлечь квадратный корень из отрицательного числа!")
            else:
                print(f"Результат: √{num1} = {math.sqrt(num1)}")
        elif choice == '7':
            print(f"Результат: {num1} % {num2} = {num1 % num2}")
        elif choice == '8':
            if num2 == 0:
                print("Ошибка: Деление на ноль невозможно!")
            else:
                print(f"Результат: {num1} // {num2} = {num1 // num2}")
        elif choice == '9':
            print(f"Результат: sin({num1}) = {math.sin(math.radians(num1))}")
        elif choice == '10':
            print(f"Результат: cos({num1}) = {math.cos(math.radians(num1))}")
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Ошибка: Неверный выбор операции.")

if __name__ == "__main__":
    main()
