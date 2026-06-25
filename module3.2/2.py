#this is polymorphism which essentially means classes that are similar in nature but have different opperations share common attributes. Essentially just interfaces
class overlap:
    def get_thing(self):
        pass
    

    
class Image(overlap):
    def __init__(self, thing):
        self.thing  = thing
    def get_thing(self):
        print(self.thing)
    def take_image(self):
        print("Taking image")

class translation(overlap):
    def __init__(self, thing):
        self.thing = thing
    def translate_text(self):
        print("Translating text")
    def get_thing(self):
        print(self.thing)

m1 = Image("hello")
m2 = translation("N")
m3 = Image("No")

def print_role(model):
    return model.get_thing()

print(print_role(m1))
print(print_role(m2))