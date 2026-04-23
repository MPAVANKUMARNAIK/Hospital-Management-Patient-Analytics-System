# 🏥 Hospital Management & Patient Analytics System

A SQL-based project designed to manage hospital records and perform data analytics on patient treatments, doctor performance, and hospital operations.
This system helps hospitals efficiently store data and extract meaningful insights.

---

## 📌 Problem Statement

Hospitals need efficient systems to manage patient records and analyze treatment data.
This project solves that by creating a structured database and performing analytical queries.

---

## 🎯 Objectives

* Design a database to store patient, doctor, and treatment data
* Perform analysis on hospital operations
* Generate insights from healthcare data

---

## 🗄️ Database Tables

### 🧑 Patients

* patient_id
* name
* age
* gender

### 👨‍⚕️ Doctors

* doctor_id
* name
* specialization

### 📅 Appointments

* appointment_id
* patient_id
* doctor_id
* date

### 💊 Treatments

* treatment_id
* patient_id
* diagnosis
* cost

---

## 🧠 Key Tasks

✔ Find most consulted doctors
✔ Calculate total revenue per month
✔ Identify most common diseases
✔ Track patient visit frequency
✔ Analyze doctor performance

---

## 🖼️ Project Screenshots

### 🔹 Database Schema / Tables

![Schema](https://github.com/MPAVANKUMARNAIK/Hospital-Management-Patient-Analytics-System/blob/main/images/schema.png?raw=true)

👉 Shows the structure of tables including Patients, Doctors, Appointments, and Treatments.

---

### 🔹 SQL Query Execution

![Query](https://github.com/MPAVANKUMARNAIK/Hospital-Management-Patient-Analytics-System/blob/main/images/query.png?raw=true)

👉 Example queries used to extract insights such as revenue, most visited doctors, and disease trends.

---

### 🔹 Analytics Output

![Analytics](https://github.com/MPAVANKUMARNAIK/Hospital-Management-Patient-Analytics-System/blob/main/images/analytics.png?raw=true)

👉 Displays analyzed results like monthly revenue, patient frequency, and doctor performance.

---

## ⚙️ Tech Stack

* SQL (MySQL / PostgreSQL)
* Database Design
* Data Analysis using Queries

---

## 🏗️ Project Structure

```id="wqkqfc"
Hospital-Management-Patient-Analytics-System/
│
├── SQL Scripts/
├── images/
│   ├── schema.png
│   ├── query.png
│   ├── analytics.png
├── README.md
```

---

## 🚀 How to Run

```sql id="t7n0nt"
-- Create Database
CREATE DATABASE hospital_db;

-- Use Database
USE hospital_db;

-- Run SQL scripts
-- (tables + insert + queries)
```

---

## 💡 Sample Queries

```sql id="g6k6kq"
-- Most consulted doctors
SELECT doctor_id, COUNT(*) AS total_visits
FROM appointments
GROUP BY doctor_id
ORDER BY total_visits DESC;

-- Monthly revenue
SELECT MONTH(date) AS month, SUM(cost) AS revenue
FROM treatments t
JOIN appointments a ON t.patient_id = a.patient_id
GROUP BY month;
```

---

## 📊 Expected Outcome

* Efficient hospital data management
* Insightful analytics for decision-making
* Improved tracking of patients and treatments

---

## 🔮 Future Enhancements

* Dashboard using Power BI / Tableau
* Integration with web application
* Real-time patient monitoring system
* Advanced analytics using Python

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve the project.

---

## 📜 License

This project is open-source under the MIT License.

---

## 👨‍💻 Author

**Pavan Kumar Naik**
