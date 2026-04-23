DROP DATABASE IF EXISTS hospital_db;
CREATE DATABASE hospital_db;
USE hospital_db;

-- USERS
CREATE TABLE users (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50)
);

INSERT INTO users VALUES ('admin','admin123');

-- PATIENTS
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10)
);

-- DOCTORS
CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    specialization VARCHAR(100)
);

-- APPOINTMENTS
CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

-- TREATMENTS
CREATE TABLE treatments (
    treatment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    diagnosis VARCHAR(100),
    cost DECIMAL(10,2),
    treatment_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

-- DATA
INSERT INTO patients (name, age, gender) VALUES
('Ravi',30,'Male'),
('Sita',25,'Female'),
('Arjun',40,'Male');

INSERT INTO doctors (name, specialization) VALUES
('Dr. Sharma','Cardiology'),
('Dr. Reddy','Orthopedics'),
('Dr. Khan','General');

INSERT INTO appointments (patient_id, doctor_id, date) VALUES
(1,1,'2025-01-10'),
(2,3,'2025-01-11'),
(1,1,'2025-02-15'),
(3,2,'2025-02-20');

INSERT INTO treatments (patient_id, doctor_id, diagnosis, cost, treatment_date) VALUES
(1,1,'Heart Disease',5000,'2025-01-10'),
(2,3,'Fever',500,'2025-01-11'),
(1,1,'Heart Disease',7000,'2025-02-15'),
(3,2,'Fracture',3000,'2025-02-20');