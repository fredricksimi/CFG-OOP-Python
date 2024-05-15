
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting")

    def roll_over(self):
        print(f"{self.name} who is {self.age} is rolling over")

bruno = Dog('Bruno', 5)
print(f"The name of the dog is {bruno.name}")
print(f"The age of the dog is {bruno.age}")

bruno.sit()
bruno.roll_over()