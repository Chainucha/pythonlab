import sqlite3
from tabulate import tabulate

cn = sqlite3.connect("electricity_db.db")  # SQLite example
cursor = cn.cursor()
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS employee (
empno VARCHAR(15),
name VARCHAR(25),
salary FLOAT PRIMARY KEY
) """
)
# Commit the changes and close the connection
cn.commit()
while True:
    choice = int(
        input(
            "1. Accept employee details\n2. Display details of a specificemployee\n3. Display details of an employee within a given salary range\n4. Exit\nEnter your choice: "
        )
    )
    if choice == 1:
        n = int(input("Enter the number of employees: "))
        for s in range(1, n + 1):
            empno, name, salary = input(
                f"Enter Employee Number, Name, and Salary ofemployee {s}: "
            ).split()
            values = (empno, name, salary)
            print(values)
            cursor.execute(
                "INSERT INTO employee (empno, name, salary)VALUES (?,?,?)", values
            )
            cn.commit()
            print("Record inserted successfully.")
    elif choice == 2:
        empno = input(f"Enter Employee Number of the employee to display details: ")
        values = (empno,)
        cursor.execute("SELECT * FROM employee WHERE empno = ?", values)

        record = cursor.fetchone()
        data = []
        if record:
            data.append(record)
            headers = ["Employee Number", "Employee Name", "Salary"]
            print(tabulate(data, headers, tablefmt="grid"))
        else:
            print("Employee not found.")
    elif choice == 3:
        min_salary, max_salary = input("Enter salary range: ").split()
        values = (min_salary, max_salary)
        cursor.execute("SELECT * FROM employeeWHERE salary BETWEEN ? AND ?", values)
        records = cursor.fetchall()
        data = []
        for record in records:
            data.append(record)
            headers = ["Employee Number", "Employee Name", "Salary"]
            print(tabulate(data, headers, tablefmt="grid"))
    elif choice == 4:
        print("Terminating..!")
        break
    else:
        print("Invalid choice..!")
        cn.close()
