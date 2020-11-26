# class Car:
#     def __init__(self):
#         self.modules = []
#         self._fc = 7
#
#     def __add__(self, other):
#         self.modules.append(other)
#         return self
#
#     def __str__(self):
#         return f'{self.modules}'
#
#     def __del__(self):
#         print('РћР±СЉРµРєС‚ СѓРґР°Р»РµРЅ')
#
#     def __setattr__(self, key, value):
#         super().__setattr__(key, value)
#         # self.__dict__[key] = value
#         print(f'Р”РѕР±Р°РІР»РµРЅ Р°С‚СЂРёР±СѓС‚ {key} СЃРѕ Р·РЅР°С‡РµРЅРёРµРј {value}')
#
#     def __getitem__(self, item):
#         return self.modules[item]
#
#     def __call__(self, price=None):
#         # self.price = price
#         print(f'\nFull car info\nmodules: {self.modules}\nprice: {price}')
#
#     def __eq__(self, other):
#         return self._fc == other
#
# car = Car()
# module1 = 'С‚РµРїР»С‹Р№ СЂСѓР»СЊ'
# module2 = 'РїР°СЂРєС‚СЂРѕРЅРёРє'
# module3 = 'СЂРѕР·РѕРІС‹Р№ СЂСѓС‡РЅРёРє'
# # car + module1  # car.modules.append(module1) # car.__add__(module1)
# # car + module2  # car.modules.append(module1)
# # car + module3  # car.modules.append(module1)
# car + module1 + module2 + module3
# car.model = 'Tesla'
# print(car[1])
# print(car)
# car(5000)
#
# print(car == 8)


# from abc import ABC, abstractmethod
# class MyAbsClass(ABC):
#     @abstractmethod
#     def my_method1(self):
#         pass
#     @abstractmethod
#     def my_method2(self):
#         pass
# class MyClass(MyAbsClass):
#     def my_method1(self):
#         print('qwe')
#     def my_method2(self):
#         print('qwe')
# mc = MyClass()


# for x in 123:  # iter? -> object->next->next->StopIteration
#     print(x)

# class Iterator:
#     def __init__(self):
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration
# qwe = Iterator()
# for i in qwe:
#     print(i)

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#
#     @property
#     def age(self):
#         # check age
#         return self._age
#     # many codes
#     # many codes
#
# human = Human('Ivan', 20)
# print(human.age)


class WinDoor:
    def __init__(self, length, width):
        self.square = length * width


class Room:
    def __init__(self, len1, len2, h):
        self.square = 2 * h * (len1 + len2)
        self.wd = []

    def add_windoor(self, w, l):
        self.wd.append(WinDoor(w, l))

    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square
        return main_square


r = Room(10, 20, 4)
print(r.square)
r.add_windoor(2, 2)
r.add_windoor(2, 1)
r.add_windoor(3, 1)
r.add_windoor(3, 2)
print(r.common_square())