from students import Student

class Botan(Student):
    def __init__(self, name, age, sex, mark, alive, power):
        self.name = name
        self.age = age
        self.sex = sex
        self.mark = mark
        self.alive = alive
        self.power = power


    def learn_hard(self):
        pass


    def __str__(self):
        return (f"{self.name}: age = {self.age}, sex = {self.sex}, "
                f"mark = {self.mark} ,alive = {self.alive}, power = {self.power}")