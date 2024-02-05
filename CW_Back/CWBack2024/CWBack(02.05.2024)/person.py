class Person:
    __first_name = ""
    __last_name = ""
    __age = 0
    __gender = ""
    __partner = None

    def init(self, full_name:str, age:int, gender):
        self.__first_name, self.__last_name = full_name.split(' ')
        self.__age = age
        self.__gender = gender

    def first_name(self):
        return self.__first_name

    def partner(self):
        return self.__partner

    def last_name(self):
        return self.__last_name

    def age(self):
        return self.__age

    def gender(self):
        return self.__gender

    

    def marry(self, partner):
        if partner is self:
            return
        if partner.gender == self.__gender:
            return
        if partner.partner or self.__partner:
            return
        if partner.age < 16 or self.__age < 16:
            return
        self.__partner = partner
        if self.__gender == "female":
            self.__last_name = partner.last_name
    
if __name__ == "__main__":
    boy = Person('John Doe', 14, 'male')
    girl = Person('Sandugash Shishikmetova', 8, 'female')
    man = Person('Muhammed Sallah', 35, 'male')
    woman = Person("Stella Young", 26, 'female')

    woman.marry(woman)