class Aminal:
    def set_age(self, age):
        self.age = age
    def get_age(self):
          return self.age
    def speak(self):
          return "gibberish"
class Dog(Aminal): # define child class
    def speak(self):
        return "wow-wow"

class Man(Aminal): # define child class
    def speak(self):
        return "How are you doing?"

def main():
    m = Man()
    m.set_age(4*2)
    d = Dog()
    d.set_age(4)
    print(m.speak())
    print(m.get_age())
    print(d.speak())
    print(d.get_age())
main()