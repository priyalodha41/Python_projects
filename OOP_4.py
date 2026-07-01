# ==========================
# Employee Management System
# ==========================

class Employee:

    next_employee_id = 1

    def __init__(self, name, age, salary):
        self.employee_id = Employee.next_employee_id
        Employee.next_employee_id += 1

        self.name = name
        self.age = age
        self.salary = salary

    def display_details(self):
        print("-" * 40)
        print(f"Employee ID      : {self.employee_id}")
        print(f"Name             : {self.name}")
        print(f"Age              : {self.age}")
        print(f"Salary           : ₹{self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print("Salary updated successfully!")

    def calculate_annual_salary(self):
        print(f"Annual Salary : ₹{self.salary * 12}")

    def work(self):
        print(f"{self.name} is working.")


# ==========================
# Developer
# ==========================

class Developer(Employee):

    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language : {self.programming_language}")

    def work(self):
        print(f"{self.name} is writing {self.programming_language} code.")


# ==========================
# Manager
# ==========================

class Manager(Employee):

    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department          : {self.department}")

    def manage_team(self):
        print(f"{self.name} is managing the {self.department} team.")

    def work(self):
        print(f"{self.name} is managing the team.")


# ==========================
# HR
# ==========================

class HR(Employee):

    def __init__(self, name, age, salary, region):
        super().__init__(name, age, salary)
        self.region = region

    def display_details(self):
        super().display_details()
        print(f"Region              : {self.region}")

    def hire_employee(self):
        print(f"{self.name} is hiring employees.")

    def work(self):
        print(f"{self.name} is hiring employees.")


# ==========================
# Main Program
# ==========================

employees = []

while True:

    print("\n========== EMPLOYEE MANAGEMENT ==========")
    print("1. Add Developer")
    print("2. Add Manager")
    print("3. Add HR")
    print("4. Display All Employees")
    print("5. Search Employee")
    print("6. Update Salary")
    print("7. Show Annual Salary")
    print("8. Show Employee Type")
    print("9. Make Employees Work")
    print("10. Delete Employee")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    # ----------------------------
    # Add Developer
    # ----------------------------

    if choice == 1:

        name = input("Name : ")
        age = int(input("Age : "))
        salary = int(input("Salary : "))
        language = input("Programming Language : ")

        developer = Developer(name, age, salary, language)
        employees.append(developer)

        print("Developer added successfully!")

    # ----------------------------
    # Add Manager
    # ----------------------------

    elif choice == 2:

        name = input("Name : ")
        age = int(input("Age : "))
        salary = int(input("Salary : "))
        department = input("Department : ")

        manager = Manager(name, age, salary, department)
        employees.append(manager)

        print("Manager added successfully!")

    # ----------------------------
    # Add HR
    # ----------------------------

    elif choice == 3:

        name = input("Name : ")
        age = int(input("Age : "))
        salary = int(input("Salary : "))
        region = input("Region : ")

        hr = HR(name, age, salary, region)
        employees.append(hr)

        print("HR added successfully!")

    # ----------------------------
    # Display Employees
    # ----------------------------

    elif choice == 4:

        if not employees:
            print("No employees found.")
        else:
            for employee in employees:
                employee.display_details()

    # ----------------------------
    # Search Employee
    # ----------------------------

    elif choice == 5:

        employee_id = int(input("Enter Employee ID : "))

        found = False

        for employee in employees:

            if employee.employee_id == employee_id:
                employee.display_details()
                found = True
                break

        if not found:
            print("Employee not found.")

    # ----------------------------
    # Update Salary
    # ----------------------------

    elif choice == 6:

        employee_id = int(input("Employee ID : "))
        new_salary = int(input("New Salary : "))

        found = False

        for employee in employees:

            if employee.employee_id == employee_id:
                employee.update_salary(new_salary)
                found = True
                break

        if not found:
            print("Employee not found.")

    # ----------------------------
    # Annual Salary
    # ----------------------------

    elif choice == 7:

        employee_id = int(input("Employee ID : "))

        found = False

        for employee in employees:

            if employee.employee_id == employee_id:
                employee.calculate_annual_salary()
                found = True
                break

        if not found:
            print("Employee not found.")

    # ----------------------------
    # Employee Type
    # ----------------------------

    elif choice == 8:

        if not employees:
            print("No employees found.")
        else:
            for employee in employees:
                print(
                    f"Employee ID : {employee.employee_id} | "
                    f"Name : {employee.name} | "
                    f"Type : {type(employee).__name__}"
                )

    # ----------------------------
    # Polymorphism
    # ----------------------------

    elif choice == 9:

        if not employees:
            print("No employees found.")
        else:
            for employee in employees:
                employee.work()

    # ----------------------------
    # Delete Employee
    # ----------------------------

    elif choice == 10:

        employee_id = int(input("Employee ID : "))

        found = False

        for employee in employees:

            if employee.employee_id == employee_id:
                employees.remove(employee)
                print("Employee deleted successfully!")
                found = True
                break

        if not found:
            print("Employee not found.")

    # ----------------------------
    # Exit
    # ----------------------------

    elif choice == 11:

        print("Thank you for using Employee Management System.")
        break

    else:
        print("Invalid Choice!")