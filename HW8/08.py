import random

class Card:
    def __init__(self, name):
        self.name = name
        self.card = []
        i = [1, 11, 21, 31, 41, 51, 61, 71, 81] #шаблон карточки
        num_s = 0
        while num_s < 3:
            j = 4
            my_list = [random.randint(el, el + 9) for el in i] #генерация строки
            while j > 0:
                my_list[random.randint(0, 8)] = ' ' #убираем лишнее
                if my_list.count(' ') == 4:
                    j = 0
            self.card.append(my_list) #генерация карточки
            num_s += 1





    def __str__(self):
        print('-----------------', self.name, '-----------------')
        return str('\n'.join(['\t'.join([str(j) for j in i])for i in self.card]))

    def prov_pc(self, num): #зачеркивание ответа пк
        for elem in self.card:
            if elem.count(num) == 1:
                i = elem.index(num)
                elem[i] = '-'
                break


    def prov_pl(self, num, answ): #проверка ответа игрока
        if answ == 'y':
            j = 0
            for elem in self.card:
                if elem.count(num) == 1:
                    i = elem.index(num)
                    elem[i] = '-'
                    j += 1
                    break
                elif j == 3:
                    print('Error. Game Over')
                    exit(-1)


        elif answ != 'y':
            for elem in self.card:
                for el in elem:
                    if el == num:
                        print('Error. Game Over')
                        exit(-1)







plaer_card = Card('Plaer')
pc_card = Card('PC')
print(plaer_card)
print(pc_card)
bag = [el for el in range(1, 91)]
while True:
    num = bag[random.randint(0, len(bag))]
    bag.remove(num)
    print('----Number: ', num, '------ y/n')
    answ = input('')
    plaer_card.prov_pl(num, answ)
    print(plaer_card)
    pc_card.prov_pc(num)
    print(pc_card)





