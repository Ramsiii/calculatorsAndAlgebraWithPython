class Circle():
    
    pi = 3.1416
    
    def __init__(self, radius = 1, unit = "cm", name="unnamed circle"):
        self.radius = radius
        self.diameter = radius * 2
        self.unit = unit
        self.name = name
        
    def get_circumference(self):
        print(f"The circumference of {self.name} is {self.radius * self.pi * 2} {self.unit}.")
        

mycircle = Circle(3.5, "inches", "a personal pizza")

print(mycircle.diameter)

mycircle.get_circumference()