import sqlite3
from tabulate import tabulate

import sqlite3
from tabulate import tabulate

# Connect to database (creates file if it doesn't exist)
con = sqlite3.connect("student1.db")
cursor = con.cursor()

# Create table 'student' if it does not exist
con.execute(
    """
CREATE TABLE IF NOT EXISTS student(
regno VARCHAR(15) PRIMARY KEY,
name VARCHAR(25),
marks1 FLOAT,
marks2 FLOAT,
marks3 FLOAT
)"""
)
con.commit()

# Menu loop
while True:
    # Display menu and get user choice
    choice = int(
        input(
            "\n1.Accept student details\n2. details of all the students\n3.Delete Display details of a particular students\n4.exit \nEnter your choice:"
        )
    )

    # ---------------- OPTION 1: Insert student details ----------------
    if choice == 1:
        n = int(input("Enter the number of students:"))

        for s in range(1, n + 1):
            # Accept student information
            regno = input(f"Enter the register number of student {s}:")
            name = input(f"Enter the name of {s}:")
            marks1, marks2, marks3 = input(
                f"Enter the marks of student {s} in three subjects:"
            ).split()

            # Prepare tuple for insertion
            values = (regno, name, marks1, marks2, marks3)

            # Insert into database
            cursor.execute(
                "INSERT INTO student(regno,name,marks1,marks2,marks3) VALUES(?,?,?,?,?)",
                values,
            )
            con.commit()

            print(
                f"Record of student with register number {regno} inserted successfully."
            )

    # ---------------- OPTION 2: Display details of all students -------
    elif choice == 2:
        cursor.execute("SELECT * FROM student")  # Fetch all records
        records = cursor.fetchall()

        data = []
        for record in records:
            data.append(record)
            headers = [
                "Register Number",
                "Name",
                "Marks of Subject 1",
                "Marks of Subject 2",
                "Marks of Subject 3",
            ]
            # Display each student record in tabular form
            print(tabulate(data, headers, tablefmt="pretty"))

    # ---------------- OPTION 3: Delete a student record ----------------
    elif choice == 3:
        rno = input("Enter regno of student to delete the record:")
        values = (rno,)

        # Delete record from table
        cursor.execute("DELETE FROM student WHERE regno = ?", values)
        con.commit()

        print(f"Record of student with register number {rno} deleted successfully.")

    # ---------------- OPTION 4: Exit program --------------------------
    elif choice == 4:
        print("Terminating....!")
        break

    # ---------------- INVALID OPTION -----------------------------------
    else:
        print("Invalid choice..!")
        con.close()
