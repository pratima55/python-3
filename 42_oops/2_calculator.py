class Calculator:
    output_sentence = "of two number is"
    def sum(self,a,b):
        print("addition",self.output_sentence ,a+b)

    def sub(self,a,b):
        print("subtraction", self.output_sentence ,a-b)   

    def mul(self,a,b):
        print("multiplication", self.output_sentence ,a*b)     

c1 = Calculator ()
c1.sum(5,9)
c1.sub(5,3)
c1.mul(5,6)
