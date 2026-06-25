class SomeClass:
    def __init__(self, thing):
        self.thing = thing
    
    @staticmethod
    def do_thing(another_thing):
        print(another_thing)
    def do_second_thing(self):
        print(self.thing)

call = SomeClass("Hello")
print(call.do_second_thing())

calling_not_class = SomeClass.do_thing("Noo class was called") # -> if not static method was used this wouldve given me an error -> I can call functions inside of classes without having to first instantiate the class seperatly