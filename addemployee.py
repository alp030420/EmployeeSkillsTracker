def add_employee():
    employee_id = int(input("Employee ID: "))
    name = input(" Employee Name: ")
    name = input(" Employee Name: ")

    cursor.execute(
        "INSERT INTO employees (employee_id, name) VALUES (?, ?)",
        (employee_id, name)
    )

    conn.commit()
    print("Employee added successfully.")
