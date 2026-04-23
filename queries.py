# Revenue per month
def get_revenue(cursor):
    cursor.execute("""
        SELECT DATE_FORMAT(treatment_date,'%Y-%m') AS month,
               SUM(cost) AS revenue
        FROM treatments
        GROUP BY month
        ORDER BY month
    """)
    return cursor.fetchall()


# Most consulted doctors (TOP 10)
def most_consulted_doctors(cursor):
    cursor.execute("""
        SELECT d.name, COUNT(a.appointment_id) AS total_visits
        FROM doctors d
        JOIN appointments a ON d.doctor_id = a.doctor_id
        GROUP BY d.name
        ORDER BY total_visits DESC
        LIMIT 10
    """)
    return cursor.fetchall()


# Most common diseases
def common_diseases(cursor):
    cursor.execute("""
        SELECT diagnosis, COUNT(*) AS count
        FROM treatments
        GROUP BY diagnosis
        ORDER BY count DESC
        LIMIT 10
    """)
    return cursor.fetchall()


# Patient visit frequency
def patient_visits(cursor):
    cursor.execute("""
        SELECT p.name, COUNT(a.appointment_id) AS visits
        FROM patients p
        JOIN appointments a ON p.patient_id = a.patient_id
        GROUP BY p.name
        ORDER BY visits DESC
        LIMIT 10
    """)
    return cursor.fetchall()