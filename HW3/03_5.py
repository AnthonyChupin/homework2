numbers = []
ind = 0
summa = 0
while True:
    if input('Выход - Q, \nЛюбая клавиша - продолжить: ').upper() == 'Q':
        break
    numbers = input("Vvedite chisla")
    numbers = numbers.split()
    while ind < len(numbers):
        try:
            numbers[ind] = int(numbers[ind])
        except ValueError:
            break
        ind = ind + 1

    for i in numbers:
        summa = summa + i
    print(summa)
    ind = 0

