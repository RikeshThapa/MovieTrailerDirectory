class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("last name " + self.last_name)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("number of toys" + str(self.number_of_toys))

dad = Parent("Thapa", "Brown")
#print(dad.last_name)
dad.show_info()

me = Child("Thapa", "Brown", 10)
me.show_info()


