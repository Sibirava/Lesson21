from human import Human

class Worker(Human):
    def __init__(self, name, age, sex, salary, alive):
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary
        self.alive = alive



    def work(self):
        pass


    def __str__(self):
        return (f"{self.name}: age = {self.age}, sex = {self.sex}, "
                f"salary = {self.salary} ,alive = {self.alive}")