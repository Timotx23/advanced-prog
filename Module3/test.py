from abc import ABC, abstractmethod
#what this system allows me to do is give attributes to a combined class which it didnt have before
class IAnimal(ABC):
    @abstractmethod
    def has_4_legs(self):
        pass

class Dog(IAnimal):
    def __init__(self, is_dog, **kwargs):
        self.is_dog = "Yeseews"
        self.breed = "Dog"
        print("Dog is being called")

        super().__init__(**kwargs)


    def has_4_legs(self):
        return True
    
        
class Cat(IAnimal):
    def __init__(self,is_feeline, **kwargs):
        self.is_feeline = "Yes"
        self.breed = "Cat"
        print("Cat is being called")
        super().__init__(**kwargs)


    def has_4_legs(self):
        return True
    

class Cat_Dog_Mix(Dog, Cat):
    def __init__(self, is_feeline, is_dog):
     
        super().__init__(
           
            is_feeline = is_feeline,
            is_dog= is_dog
        
        )
    def has_4_legs(self):
    
        return f"Yes the {self.breed} has 4 legs. But is it a feeline? {self.is_feeline} and also is it a dog? {self.is_dog}" 


is_dog = "Yes"
is_Feeline = "No"  
cla = Cat_Dog_Mix( is_Feeline, is_dog)

print(Cat_Dog_Mix.mro())
print(cla.has_4_legs())