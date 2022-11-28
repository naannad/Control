# 14 задача
from datetime import date


class Person():
    def __init__(self, surname, hb):
        self.surname = surname
        self.hb = hb

    def info_peron(self):
        print(f"Фамилия: {self.surname}, дата дня рождения: {self.hb}")

    def info_age(self, year):
        return int(year) - int(self.hb[-4:])


class Мatriculant(Person):
    def __init__(self, surname, hb, faculty):
        self.faculty = faculty
        super().__init__(surname, hb)

    def info_matriculant(self, surname, hb, faculty):
        print(f"Вот вся ваша информация: {self.surname, self.hb, self.faculty }")


class Student(Person):
    def __init__(self, surname, hb, faculty, course):
        self.faculty = faculty
        self.course = course
        super().__init__(surname, hb)

    def info_student(self, surname,hb, faculty, course):
        print(f"Вот вся ваша информация: {self.surname, self.hb, self.faculty, self.course}")


class Тeacher(Person):
    def __init__(self, surname, hb, faculty, job, experience):
        self.faculty = faculty
        self.job = job
        self.experience = experience
        super().__init__(surname,hb)

    def info_teacher(self):
        print(f"Вот вся ваша информация: {self.surname, self.hb, self.faculty, self.job, self.experience }")


nastya = Person("Dor", "07.02.2004")
print(nastya.info_age(2022))
print(nastya.info_peron())

Yana = Мatriculant("Мар", "16.02.2004", "Безопасник")
print(Yana.info_age(2022))
print(Yana.info_peron())
print(Yana.info_matriculant("Мар", "16.02.2004", "Безопасник"))




