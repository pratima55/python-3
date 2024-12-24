#WAP to calculate staff salary with bonus, and print staff name and total salary


employe_data = [
    {"name":"ram", "salary":35000, "bonus": 2},
    {"name":"hari", "salary":30000, "bonus": 5},
    {"name":"shyam", "salary":80000, "bonus": 10},
    {"name":"gopal", "salary":62000, "bonus": 23},

]
# def total_salary(salary, bonus):
#     return salary + bonus/100*salary

# for item in employe_data:
#     name = item["name"]
#     salary = item["salary"]
#     bonus = item["bonus"]
#     total_salary_var= total_salary(salary,bonus)

#     print("*******************")
#     print(f"staff name {name} with salary {salary}, bonus {bonus}%, total salary {total_salary_var} ")

employe_data = [
    {"name":"ram", "salary":35000, "bonus": 2},
    {"name":"hari", "salary":30000, "bonus": 5},
    {"name":"shyam", "salary":80000, "bonus": 10},
    {"name":"gopal", "salary":62000, "bonus": 23},

]
class Employee:

    def __init__(self,name,salary,bonus):
        self.user_name = name
        self.salary = salary
        self.bonus = bonus


    def calculate_salary(self):
        output = self.salary + self.bonus/100*self.salary
        return output

for emp_data in employe_data:
    print("************************")
    emp_obj = Employee(emp_data["name"], emp_data["salary"], emp_data["bonus"])
    output = emp_obj.calculate_salary()
    print(f"{emp_data["name"]} total salary with bonus)",output)

ram_obj = Employee("ram",43000,9)  
output = ram_obj.calculate_salary()     
print("total salary with bonus:", output)
    


