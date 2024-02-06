class Acc:
    __balance = {}
    

    def __init__(self, __tenge, __dolar, __euro , __yen):
        self.__balance["tenge"] = __tenge
        self.__balance["dolar"] = __dolar
        self.__balance["euro"] = __euro
        self.__balance["yen"] = __yen


    def get_balance(self):
        return self.__balance

    

class Monee:
    __volume = 0
    __currency = ''

tg = 2000

kaspi = Acc(tg, )    