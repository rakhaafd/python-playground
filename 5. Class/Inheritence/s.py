class Person:
    name = 'test'

class Employee (Person):
    gaji = 100

person1 = Person()
employee1 = Employee()

print(person1.name)
# print(person1.gaji) # jika parent, tidak akan bisa mengakses child
print(employee1.gaji)
print(employee1.name) # jika child, bisa mengakses class variable milik parent 