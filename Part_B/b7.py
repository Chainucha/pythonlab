import sqlite3


# ------------------------------------------------------------
# Create table if not exists
# ------------------------------------------------------------
def create_table():
    try:
        conn = sqlite3.connect("electricity3_db.db")
        cursor = conn.cursor()

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS electricity_bill1(
            TariffCode TEXT,
            Customer_Name TEXT,
            Meter_Number TEXT PRIMARY KEY,
            Previous_Reading FLOAT,
            Current_Reading FLOAT
        )"""
        )

        conn.commit()
        conn.close()
        print("Table 'electricity_bill1' created successfully.")

    except Exception as e:
        print(f"Error: {str(e)}")


# ------------------------------------------------------------
# Insert customer details into the database
# ------------------------------------------------------------
def insert_customer_details():
    try:
        meter_number = input("Enter Meter Number: ")
        tariff_code = input("Enter Tariff Code: ")
        customer_name = input("Enter Customer Name: ")
        previous_reading = float(input("Enter Previous Reading: "))
        current_reading = float(input("Enter Current Reading: "))

        conn = sqlite3.connect("electricity3_db.db")
        cursor = conn.cursor()

        cursor.execute(
            """INSERT INTO electricity_bill1
            (TariffCode, Customer_Name, Meter_Number, Previous_Reading, Current_Reading)
            VALUES (?, ?, ?, ?, ?)
        """,
            (
                tariff_code,
                customer_name,
                meter_number,
                previous_reading,
                current_reading,
            ),
        )

        conn.commit()
        conn.close()
        print("Customer details inserted successfully.")

    except Exception as e:
        print(f"Error: {str(e)}")


# ------------------------------------------------------------
# Update customer details based on meter number
# ------------------------------------------------------------
def update_customer_details_by_meter_number():
    try:
        meter_number = input("Enter meter number to update: ")
        new_customer_name = input("Enter new customer name: ")
        new_tariff_code = input("Enter new Tariff Code: ")

        conn = sqlite3.connect("electricity3_db.db")
        cursor = conn.cursor()

        cursor.execute(
            """UPDATE electricity_bill1
                          SET Customer_Name = ?, TariffCode = ?
                          WHERE Meter_Number = ?""",
            (new_customer_name, new_tariff_code, meter_number),
        )

        conn.commit()
        conn.close()
        print("Customer details updated successfully.")

    except Exception as e:
        print(f"Error: {str(e)}")


# ------------------------------------------------------------
# Calculate electricity bill based on tariff code
# ------------------------------------------------------------
def calculate_customer_bill(meter_number):
    try:
        conn = sqlite3.connect("electricity3_db.db")
        cursor = conn.cursor()

        cursor.execute(
            """SELECT Previous_Reading, Current_Reading, TariffCode
                          FROM electricity_bill1 WHERE Meter_Number = ?""",
            (meter_number,),
        )
        row = cursor.fetchone()

        if row:
            previous_reading, current_reading, tariff_code = row
            units_consumed = current_reading - previous_reading

            # Bill Calculation for Tariff LT1
            if tariff_code == "LT1":
                if units_consumed <= 30:
                    bill = units_consumed * 2.0
                elif units_consumed <= 100:
                    bill = (30 * 2.0) + (units_consumed - 30) * 3.5
                elif units_consumed <= 200:
                    bill = (30 * 2.0) + (70 * 3.5) + (units_consumed - 100) * 4.5
                else:
                    bill = (
                        (30 * 2.0)
                        + (70 * 3.5)
                        + (100 * 4.5)
                        + (units_consumed - 200) * 5.0
                    )

            # Bill Calculation for Tariff LT2
            else:
                if units_consumed <= 30:
                    bill = units_consumed * 3.5
                elif units_consumed <= 100:
                    bill = (30 * 3.5) + (units_consumed - 30) * 5.0
                elif units_consumed <= 200:
                    bill = (30 * 3.5) + (70 * 5.0) + (units_consumed - 100) * 6.0
                else:
                    bill = (
                        (30 * 3.5)
                        + (70 * 5.0)
                        + (100 * 6.0)
                        + (units_consumed - 200) * 7.5
                    )

            print(f"\nCustomer Meter Number: {meter_number}")
            print(f"Units Consumed: {units_consumed}")
            print(f"Bill Amount: ₹{bill:.2f}")

        else:
            print("Customer not found.")

        conn.close()

    except Exception as e:
        print(f"Error: {str(e)}")


# ------------------------------------------------------------
# MAIN MENU LOOP
# ------------------------------------------------------------
create_table()

while True:
    print("\n**************** Menu ********************")
    print("1. Insert Customer Details")
    print("2. Update Customer Details")
    print("3. Calculate Customer Bill")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        insert_customer_details()

    elif choice == "2":
        update_customer_details_by_meter_number()

    elif choice == "3":
        meter_number = input("Enter the meter number: ")
        calculate_customer_bill(meter_number)

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please select a valid option.")
