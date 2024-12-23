class Calculator :
    
    def __init__(self,first_number,operator, second_number):
        print("this is initializing....")
        self.first_number= first_number
        self.second_number= second_number
        self.operator = operator

    def result(self):
        if self.operator== "+":
            return self.add()
        
        elif self.operator == "-":
            return self.subtract()
        
        elif self.operator == "*":
            return self.multiplication()
        
        elif self.operator == "/":
            return self.division()


    def add(self):
        return self.first_number + self.second_number
    
    def subtract(self):
        return self.first_number - self.second_number
    
    def multiplication(self):
        return self.first_number * self.second_number
    
    def division(self):
        return self.first_number / self.second_number
    


cal_obj = Calculator(4,"+",8)
add_output= cal_obj.result()

cal_obj = Calculator(5,"-",9)
sub_output = cal_obj.result()

cal_obj = Calculator(5,"*",9)
mul_output = cal_obj.result()

cal_obj = Calculator(10,"/",5)
div_output = cal_obj.result()

print("calculation of two number is ", add_output)
print("subtraction of two number is ", sub_output)
print("multiplication of two number is ", mul_output)
print("division of two number is ", div_output)