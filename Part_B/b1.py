from tabulate import tabulate


class Employee:
    def __init__(self, empno, name, depname, designation, age, salary):
        # Initialize employee details
        self.empno = empno
        self.name = name
        self.depname = depname
        self.designation = designation
        self.age = age
        self.salary = salary

    @staticmethod
    def accept_details():
        """
        Accepts employee details from the user in a single input line.
        Returns an Employee object created using the entered details.
        """
        empno, name, depname, designation, age, salary = input(
            "Enter employee details (empno name depname designation age salary): "
        ).split()

        return Employee(empno, name, depname, designation, age, salary)

    @staticmethod
    def search_employee(employees, empno):
        """
        Searches for an employee in the list by employee number.
        Returns the employee object if found, otherwise None.
        """
        return next((emp for emp in employees if emp.empno == empno), None)

    @staticmethod
    def display_employee(emp):
        """
        Displays the details of a single employee using the tabulate library
        in a formatted table layout.
        """
        headers = [
            "Employee Number",
            "Name",
            "Department Name",
            "Designation",
            "Age",
            "Salary",
        ]

        # Data for one employee (one row table)
        data = [
            [emp.empno, emp.name, emp.depname, emp.designation, emp.age, emp.salary]
        ]

        print(tabulate(data, headers, tablefmt="fancy_grid"))


# -------- Main Program --------

# Number of employees to accept
n = int(input("Enter the number of employees: "))

# Accept details of n employees and store them in a list
employees = [Employee.accept_details() for _ in range(n)]

# Search employee by employee number
empno_to_search = input("\nEnter the employee number to search: ")

# Look for the employee in the list
found_employee = Employee.search_employee(employees, empno_to_search)

# Display result
if found_employee:
    Employee.display_employee(found_employee)
else:
    print("Employee not found.")
