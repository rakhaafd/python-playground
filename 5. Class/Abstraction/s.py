from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
      # Tidak mengimplementasikan speak()
      def speak(self):
           print('dawg')
# Ini akan menghasilkan error
dog = Dog()
dog.speak()

# INTINYA abstract method itu merupakan acuan untuk subclass dibawahnya, misal di abstact method ada method speak. nah berarti subclass di bawahnya harus memilikinya.