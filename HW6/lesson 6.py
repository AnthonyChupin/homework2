import time


# def print_human_name(human):
#     print(human['name'])
#
# h1 = {'name': 'ABS'}
# h2 = {'name': 'asd'}
# h3 = {'full_name': 'zsdzd'}
#
# print_human_name(h1)
# print_human_name(h3)


class Phone:  # CamelStyle
    def __init__(self, model):
        self.model_phone = model
        self._loading()
        self.__id = 654654

    def get_id(self):
        return self.__id

    def _loading(self):
        print(self.model_phone, 'loading...')

    def call(self):
        print(self.model_phone, 'calling')


# my_phone1 = Phone('nokia1100')
# my_phone1.call()
# print(my_phone1.get_id())
# print(my_phone1._Phone__id)  # object._ClassName__foo

# my_phone2 = Phone('nokia3110')
# print(my_phone1.model_phone)
# print(my_phone2.model_phone)
# my_phone1.call()
# my_phone2.call()

# my_list1 = list()
# my_list2 = list()


class SmartPhone(Phone):

    def sms(self):
        print('smsing')

    def email(self):
        print('emailing')


# sphone = SmartPhone('nokia6600')
# print(sphone.get_id())
# sphone.email()


class Iphone(SmartPhone):
    def __init__(self, model):
        super().__init__(model)
        print('show_logo')

    def player(self):
        print('music')

    def browser(self, web_site):
        print('browser', web_site)

    def sms(self):
        print('Imessage sending')


# iphone = Iphone('6')
# iphone.player()
# iphone.browser('qwe')
# iphone.sms()


class NextPhone(Iphone):
    def touch_id(self):
        print('touch_id')


class Huawei(NextPhone):
    pass


class Samsung(NextPhone):
    pass


# pocofone = Huawei('qwe')
# pocofone.asd = 0
# print(pocofone)

#
# class Player:
#     def player(self):
#         print('player')
#     def qwe(self):
#         print('player won')
#
# class Navigator:
#     def navigator(self):
#         print('navigator')
#     def qwe(self):
#         print('navigator won')
#
# class MPhone(Player, Navigator):
#     def mphone(self):
#         print('mphone')
#
#
# mp = MPhone()
# mp.player()
# mp.navigator()
# mp.mphone()
# mp.qwe()


class Auto:
    def auto_start(self, param, param2=None):
        if param2 is None:
            print(param)
        else:
            print(param + param2)


auto = Auto()
auto.auto_start(10)
auto.auto_start(10, 50)