import person

class Teacher(person.Person):
    _subject = ""
    _instance = None

    def new(cls, full_name, age, gender, subject):
        if cls._instance is None:
            cls._instance = super().new(cls)
        return cls._instance

    def init(self, full_name: str, age: int, gender, subject):
        super().init(full_name, age, gender)
        self._subject = subject

vitaliy = Teacher("Vitaliy Nemikin", 39, "male", "python")
print(vitaliy)
Altynay = Teacher("Altynay Altynay", 22, 'female', "html")
print(Altynay)