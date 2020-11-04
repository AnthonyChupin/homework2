time = int(input("введите время в секундах "))
hours = time//3600
minut = time%3600//60
second = time%3600%60

new_time = print(f'часы {hours} минуты {minut} секунды {second}')