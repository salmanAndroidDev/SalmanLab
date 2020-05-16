class Salary:
    def __init__(self, hourly_income, work_per_week):
        self.__hourly_income = hourly_income
        self.__work_per_week = work_per_week

    def get_monthly_income(self):
        return self.__hourly_income * (self.__work_per_week * 4)    

class Employee:
    def __init__(self, name, sal):
        self.__name = name
        self.__income_info = sal

    def print_info(self):
        info = """
        name: {}
        monthly Income: {}""".format(self.__name, self.__income_info.get_monthly_income())
        print(info)


sal = Salary(60, 80)
emp = Employee("Salman", sal)
emp.print_info()