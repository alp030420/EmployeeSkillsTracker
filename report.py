# Report by Skill Level
def skill_report():

    level = input("Enter skill level to report (Beginner, Intermediate, Advanced): ")

    cursor.execute("""
    SELECT e.name,
           s.skill_name
    FROM employees e
    JOIN skills_s
    ON e.employee_id = s.employee_id
    WHERE s.skill_level = ?
    """, (level,))

    results = cursor.fetchall()

    print(f"\nEmployees with {level} skills:")

    for employee in results:
        print(employee)
