class Circle():
    
    pi = 3.1416
    
    def __init__(self, radius = 1, unit = "cm", name="unnamed circle"):
        self.radius = radius
        self.unit = unit
        self.name = name
    
    def get_diameter(self):
        print(f"The diameter of {self.name} is {self.radius *2}.")
           
    def get_circumference(self):
        print(f"The circumference of {self.name} is {self.radius * Circle.pi * 2} {self.unit}.")
        
    def get_area(self):
        print(f"The area of {self.name} is {self.radius ** 2 * Circle.pi} square {self.unit}.")
        

if __name__ == '__main__':
    
    mycircle = Circle(3.5, "inches", "a personal pizza")

    mycircle.get_diameter()
    mycircle.get_circumference()
    mycircle.get_area()