# soal 1 program peliharaan

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

anjing1 = Dog('max', 'golden retriever')
anjing2 = Dog('bella', 'bulldog')

print(anjing1.name)
print(anjing1.breed)
print(anjing2.name)
print(anjing2.breed)

# soal 2 program mobil
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_info(self):
        print(f"mobil {self.make} {self.model} buatan tahun {self.year} siap digunakan")

mobil1 = Car('toyota', 'corolla', '2020')
mobil2 = Car('honda', 'civic', '2022')

mobil1.car_info()
mobil2.car_info()