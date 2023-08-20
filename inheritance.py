#Create a class Chef with object functions
class Chef:
    def make_chicken(self):
        print("The chef makes a chicken!")

    def make_salad(self):
        print("The chef makes a salad!")

    def make_special_dish(self):
        print("The chef makes korean food!")
#Create an object myChef
myChef = Chef()
myChef.make_chicken()

#Create a chinese chef who can make what a classic chef does and more
#Inherits the class Chef
class ChineseChef(Chef):
    def make_noodles(self):
        print("The chef makes Noodles!")
#You can overwrite object functins from master class
    def make_special_dish(self):
            print("The chef makes orange chicken!")
#The Chinese chef is able to make chicken because of inheritance
myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_special_dish()