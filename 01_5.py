doh = int(input("введите выручку "))
rash = int(input("введите издержки "))
if rash>doh:
    print ("ваша фирма убыточна ")
elif rash == doh:
    print ("доход равен нулю")
else:
    print ("вы в плюсе. Ваш доход составил ", doh-rash, "денег")
    rab = int(input("колличество сотрудников компании? "))
    print("Выручка на одного сотрудника составила ", (doh - rash)/rab, "денег")
