class Calculate():
    def __init__(self,length,breadth,radius):
        self.length= length
        self.breadth = breadth
        self.radius = radius
        

    def area_rectangle(self):
        return  self.length * self.breadth  
          
    
    def area_square(self):
        return self.length * self.length
        
    
    def area_circle(self):
       return 3.14*(self.radius**2)
        
    
# r1 = Calculate(20,30,5)
# s1 = Calculate(20,30,5)
# c1= Calculate(20,30,5)
length = int(input("Enter the length: "))
breadth = int(input("Enter th breadth: "))
radius = int(input("Enter the radius: "))

r1 = Calculate(length , breadth, radius)
s1 = Calculate(length , breadth, radius)
c1 = Calculate(length , breadth, radius)


print("Area of rectangle is: ",r1.area_rectangle())
print("Area of square is: ",s1.area_square())
print("Area of circle is: ",c1.area_circle())
