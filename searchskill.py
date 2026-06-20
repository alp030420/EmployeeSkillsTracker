def search_skill():
    skill = input("Enter skill name: ")

    cursor.execute("""
    SELECT e.name,
           s.skill_name,
           s.skill_level
    FROM employees e
    JOIN skills s
    ON e.employee_id = s.employee_id
    WHERE s.skill_name = ?
    """, (skill,))

    results = cursor.fetchall()

    for result in results:
        print(result)