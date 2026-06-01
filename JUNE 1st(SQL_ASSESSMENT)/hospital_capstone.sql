CREATE DATABASE hospital_capstone_db;
USE hospital_capstone_db;

-- patients
CREATE TABLE patients
(
 patient_id INT PRIMARY KEY,
 patient_name VARCHAR(100),
 gender VARCHAR(10),
 age INT,
 city VARCHAR(50),
 phone VARCHAR(15)
);
-- departments
CREATE TABLE departments
(
 department_id INT PRIMARY KEY,
 department_name VARCHAR(100)
);
-- doctors
CREATE TABLE doctors
(
 doctor_id INT PRIMARY KEY,
 doctor_name VARCHAR(100),
 specialization VARCHAR(100),
 department_id INT,
 consultation_fee DECIMAL(10,2)
);
-- appointments
CREATE TABLE appointments
(
 appointment_id INT PRIMARY KEY,
 patient_id INT,
 doctor_id INT,
 appointment_date DATE,
 appointment_status VARCHAR(30)
);
-- treatments
CREATE TABLE treatments
(
 treatment_id INT PRIMARY KEY,
 appointment_id INT,
 treatment_name VARCHAR(100),
 treatment_cost DECIMAL(10,2)
);
-- bills
CREATE TABLE bills
(
 bill_id INT PRIMARY KEY,
 patient_id INT,
 appointment_id INT,
 bill_date DATE,
 total_amount DECIMAL(10,2),
 bill_status VARCHAR(30)
);
-- payments
CREATE TABLE payments
(
 payment_id INT PRIMARY KEY,
 bill_id INT,
 payment_mode VARCHAR(30),
 paid_amount DECIMAL(10,2),
 payment_status VARCHAR(30)
);

-- Departments(5 records)
INSERT INTO departments (department_id, department_name) VALUES 
(1, 'Cardiology'),
(2, 'Pediatrics'),
(3, 'Orthopedics'),
(4, 'Dermatology'),
(5, 'General Medicine');

-- Patients(12 records)
INSERT INTO patients (patient_id, patient_name, gender, age, city, phone) VALUES 
(1, 'Amit Kumar', 'Male', 45, 'Hyderabad', '9876543210'),
(2, 'Priya Singh', 'Female', 28, 'Mumbai', '9876543211'),
(3, 'Ravi Teja', 'Male', 35, 'Hyderabad', '9876543212'),
(4, 'Sneha Reddy', 'Female', 52, 'Hyderabad', '9876543213'),
(5, 'Vijay Joshi', 'Male', 61, 'Pune', '9876543214'),
(6, 'Ananya Sen', 'Female', 12, 'Kolkata', '9876543215'),
(7, 'Rahul Dravid', 'Male', 48, 'Bangalore', '9876543216'),
(8, 'Sunita Williams', 'Female', 40, 'Delhi', '9876543217'),
(9, 'Rajesh Koothrapali', 'Male', 33, 'Mumbai', '9876543218'),
(10, 'Kavitha Ram', 'Female', 67, 'Chennai', '9876543219'),
(11, 'Suresh Raina', 'Male', 39, 'Ghaziabad', '9876543220'),
(12, 'Mahendra Dhoni', 'Male', 44, 'Ranchi', '9876543221');

-- Doctors(8 records)
INSERT INTO doctors (doctor_id, doctor_name, specialization, department_id, consultation_fee) VALUES 
(101, 'Dr. Arvind Sharma', 'Cardiologist', 1, 1000.00),
(102, 'Dr. Meera Reddy', 'Cardiologist', 1, 1200.00),
(103, 'Dr. S. K. Gupta', 'Pediatrician', 2, 600.00),
(104, 'Dr. Anita Desai', 'Orthopedic Surgeon', 3, 900.00),
(105, 'Dr. Rohan Verma', 'Dermatologist', 4, 800.00),
(106, 'Dr. Pooja Hegde', 'General Physician', 5, 500.00),
(107, 'Dr. Vikram Rao', 'Orthopedic Surgeon', 3, 950.00),
(108, 'Dr. Neha Kapoor', 'General Physician', 5, 500.00);

-- Appointments(20 records)
INSERT INTO appointments (appointment_id, patient_id, doctor_id, appointment_date, appointment_status) VALUES 
(1001, 1, 101, '2026-01-05', 'Completed'),
(1002, 2, 103, '2026-01-06', 'Completed'),
(1003, 3, 102, '2026-01-10', 'Completed'),
(1004, 4, 101, '2026-01-12', 'Cancelled'), 
(1005, 5, 104, '2026-01-15', 'Completed'),
(1006, 6, 103, '2026-01-18', 'Completed'),
(1007, 7, 107, '2026-01-20', 'Completed'),
(1008, 8, 105, '2026-01-22', 'Completed'),
(1009, 9, 106, '2026-01-25', 'Completed'),
(1010, 1, 102, '2026-02-02', 'Completed'),
(1011, 10, 101, '2026-02-05', 'Completed'),
(1012, 11, 108, '2026-02-10', 'Completed'),
(1013, 3, 102, '2026-02-12', 'Completed'),
(1014, 2, 105, '2026-02-15', 'Cancelled'), 
(1015, 5, 104, '2026-02-18', 'Completed'),
(1016, 7, 107, '2026-02-20', 'Completed'),
(1017, 8, 106, '2026-02-22', 'Completed'),
(1018, 4, 101, '2026-02-25', 'Completed'),
(1019, 12, 107, '2026-02-28', 'No Show'), 
(1020, 1, 101, '2026-03-02', 'Scheduled');

-- Treatments(15 records)
INSERT INTO treatments (treatment_id, appointment_id, treatment_name, treatment_cost) VALUES 
(501, 1001, 'ECG and Consultation', 1500.00),
(502, 1002, 'Pediatric Checkup', 600.00),
(503, 1003, 'Angioplasty Followup', 3000.00),
(504, 1005, 'Physiotherapy Session', 1200.00),
(505, 1006, 'Vaccination', 800.00),
(506, 1007, 'Knee X-Ray & Dressing', 2500.00),
(507, 1008, 'Acne Laser Treatment', 4500.00),
(508, 1009, 'General Health Screening', 1000.00),
(509, 1010, 'Echocardiogram', 5000.00),
(510, 1011, 'Cardiac CT Scan', 12000.00),
(511, 1012, 'Viral Fever Management', 700.00),
(512, 1013, 'Heart Rate Monitoring', 2000.00),
(513, 1015, 'Spine Alignment Extra', 3500.00),
(514, 1016, 'Fracture Plastering', 8000.00),
(515, 1017, 'Diabetes Checkup', 900.00);

-- Bills(15 Records) 
INSERT INTO bills (bill_id, patient_id, appointment_id, bill_date, total_amount, bill_status) VALUES 
(901, 1, 1001, '2026-01-05', 2500.00, 'Paid'),       
(902, 2, 1002, '2026-01-06', 1200.00, 'Paid'),       
(903, 3, 1003, '2026-01-10', 4200.00, 'Paid'),       
(904, 4, 1004, '2026-01-12', 1000.00, 'Unpaid'),     
(905, 5, 1005, '2026-01-15', 2100.00, 'Paid'),       
(906, 6, 1006, '2026-01-18', 1400.00, 'Paid'),       
(907, 7, 1007, '2026-01-20', 3450.00, 'Paid'),       
(908, 8, 1008, '2026-01-22', 5300.00, 'Partially Paid'), 
(909, 9, 1009, '2026-01-25', 1500.00, 'Paid'),       
(910, 1, 1010, '2026-02-02', 6200.00, 'Paid'),       
(911, 10, 1011, '2026-02-05', 13000.00, 'Paid'),     
(912, 11, 1012, '2026-02-10', 1200.00, 'Paid'),      
(913, 3, 1013, '2026-02-12', 3200.00, 'Paid'),       
(914, 5, 1015, '2026-02-18', 4400.00, 'Paid'),       
(915, 7, 1016, '2026-02-20', 8950.00, 'Unpaid');     

-- Payements(15 records)
INSERT INTO payments (payment_id, bill_id, payment_mode, paid_amount, payment_status) VALUES 
(701, 901, 'Cash', 2500.00, 'Success'),
(702, 902, 'UPI', 1200.00, 'Success'),
(703, 903, 'Card', 4200.00, 'Success'),
(704, 905, 'UPI', 2100.00, 'Success'),
(705, 906, 'Cash', 1400.00, 'Success'),
(706, 907, 'Card', 3450.00, 'Success'),
(707, 908, 'UPI', 3000.00, 'Success'),   
(708, 909, 'Cash', 1500.00, 'Success'),
(709, 910, 'UPI', 6200.00, 'Success'),
(710, 911, 'Net Banking', 13000.00, 'Success'),
(711, 912, 'UPI', 1200.00, 'Success'),
(712, 913, 'Card', 3200.00, 'Success'),
(713, 914, 'Cash', 4400.00, 'Success'),
(714, 901, 'UPI', 0.00, 'Failed'),       
(715, 904, 'UPI', NULL, 'Pending'); 

-- PART 1:BASIC QUERIES

-- 1. Display all patients.
SELECT * FROM patients;

-- 2. Display all doctors.
SELECT * FROM doctors;

-- 3. Find patients from Hyderabad.
SELECT * FROM patients WHERE city = 'Hyderabad';

-- 4. Find doctors from Cardiology department.
SELECT * FROM doctors 
WHERE department_id = (SELECT department_id FROM departments WHERE department_name = 'Cardiology');

-- 5. Find appointments scheduled after 2026-01-01.
SELECT * FROM appointments WHERE appointment_date > '2026-01-01';

-- 6. Find cancelled appointments.
SELECT * FROM appointments WHERE appointment_status = 'Cancelled';

-- 7. Find bills where total amount is greater than ₹5,000.
SELECT * FROM bills WHERE total_amount > 5000;

-- 8. Find payments made using UPI.
SELECT * FROM payments WHERE payment_mode = 'UPI';

-- 9. Display patients aged between 30 and 50.
SELECT * FROM patients WHERE age BETWEEN 30 AND 50;

-- 10. Display doctors with consultation fee above ₹800.
SELECT * FROM doctors WHERE consultation_fee > 800;

-- PART 2:AGGREGRATE QUERIES

-- 11. Count total patients.
SELECT COUNT(*) AS total_patients FROM patients;

-- 12. Count total doctors.
SELECT COUNT(*) AS total_doctors FROM doctors;

-- 13. Count total appointments.
SELECT COUNT(*) AS total_appointments FROM appointments;

-- 14. Find average consultation fee.
SELECT AVG(consultation_fee) AS average_consultation_fee FROM doctors;

-- 15. Find highest treatment cost.
SELECT MAX(treatment_cost) AS highest_treatment_cost FROM treatments;

-- 16. Find total billing amount.
SELECT SUM(total_amount) AS total_billing_amount FROM bills;

-- 17. Find total paid amount.
SELECT SUM(paid_amount) AS total_paid_amount FROM payments WHERE payment_status = 'Success';

-- 18. Count patients by city.
SELECT city, COUNT(*) AS patient_count FROM patients GROUP BY city;

-- 19. Count doctors by specialization.
SELECT specialization, COUNT(*) AS doctor_count FROM doctors GROUP BY specialization;

-- 20. Count appointments by status.
SELECT appointment_status, COUNT(*) AS appointment_count FROM appointments GROUP BY appointment_status;

-- PART 3-JOINS

-- 21. Display patient name with appointment date and status.
SELECT p.patient_name, a.appointment_date, a.appointment_status
FROM patients p
JOIN appointments a ON p.patient_id = a.patient_id;

-- 22. Display doctor name with department name.
SELECT d.doctor_name, dep.department_name
FROM doctors d
JOIN departments dep ON d.department_id = dep.department_id;

-- 23. Display patient name, doctor name, and appointment date.
SELECT p.patient_name, d.doctor_name, a.appointment_date
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
JOIN doctors d ON a.doctor_id = d.doctor_id;

-- 24. Display appointment ID with treatment name and cost.
SELECT appointment_id, treatment_name, treatment_cost FROM treatments;

-- 25. Display bill ID with patient name and total amount.
SELECT b.bill_id, p.patient_name, b.total_amount
FROM bills b
JOIN patients p ON b.patient_id = p.patient_id;

-- 26. Display bill ID with payment mode, paid amount, and payment status.
SELECT bill_id, payment_mode, paid_amount, payment_status FROM payments;

-- 27. Create a full appointment report.
SELECT 
    p.patient_name,
    d.doctor_name,
    dep.department_name,
    a.appointment_date,
    a.appointment_status,
    t.treatment_name,
    t.treatment_cost,
    b.total_amount AS bill_amount,
    pay.payment_status
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
JOIN doctors d ON a.doctor_id = d.doctor_id
JOIN departments dep ON d.department_id = dep.department_id
LEFT JOIN treatments t ON a.appointment_id = t.appointment_id
LEFT JOIN bills b ON a.appointment_id = b.appointment_id
LEFT JOIN payments pay ON b.bill_id = pay.bill_id;

-- PART-4:GROUP BY and HAVING

-- 28. Count appointments by doctor.
SELECT d.doctor_name, COUNT(a.appointment_id) AS total_appointments
FROM doctors d
LEFT JOIN appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id, d.doctor_name;

-- 29. Count appointments by department.
SELECT dep.department_name, COUNT(a.appointment_id) AS total_appointments
FROM departments dep
LEFT JOIN doctors d ON dep.department_id = d.department_id
LEFT JOIN appointments a ON d.doctor_id = a.doctor_id
GROUP BY dep.department_id, dep.department_name;

-- 30. Total revenue by department.
SELECT dep.department_name, COALESCE(SUM(p.paid_amount), 0) AS total_revenue
FROM departments dep
LEFT JOIN doctors d ON dep.department_id = d.department_id
LEFT JOIN appointments a ON d.doctor_id = a.doctor_id
LEFT JOIN bills b ON a.appointment_id = b.appointment_id
LEFT JOIN payments p ON b.bill_id = p.bill_id AND p.payment_status = 'Success'
GROUP BY dep.department_id, dep.department_name;

-- 31. Total treatment cost by treatment name.
SELECT treatment_name, SUM(treatment_cost) AS total_cost
FROM treatments
GROUP BY treatment_name;

-- 32. Total billing by city.
SELECT p.city, SUM(b.total_amount) AS total_billing
FROM patients p
JOIN bills b ON p.patient_id = b.patient_id
GROUP BY p.city;

-- 33. Doctors having more than 2 appointments.
SELECT d.doctor_name, COUNT(a.appointment_id) AS total_appointments
FROM doctors d
JOIN appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id, d.doctor_name
HAVING COUNT(a.appointment_id) > 2;

-- 34. Departments generating revenue greater than ₹20,000.
SELECT dep.department_name, COALESCE(SUM(p.paid_amount), 0) AS total_revenue
FROM departments dep
JOIN doctors d ON dep.department_id = d.department_id
JOIN appointments a ON d.doctor_id = a.doctor_id
JOIN bills b ON a.appointment_id = b.appointment_id
JOIN payments p ON b.bill_id = p.bill_id
WHERE p.payment_status = 'Success'
GROUP BY dep.department_id, dep.department_name
HAVING total_revenue > 20000;

-- 35. Cities having more than 2 patients.
SELECT city, COUNT(patient_id) AS total_patients
FROM patients
GROUP BY city
HAVING COUNT(patient_id) > 2;

-- PART 5:SUBQUERIES
-- 36. Find patients who have appointments.
SELECT * FROM patients 
WHERE patient_id IN (SELECT DISTINCT patient_id FROM appointments);

-- 37. Find patients who never booked appointments.
SELECT * FROM patients 
WHERE patient_id NOT IN (SELECT DISTINCT patient_id FROM appointments);

-- 38. Find doctors who have no appointments.
SELECT * FROM doctors 
WHERE doctor_id NOT IN (SELECT DISTINCT doctor_id FROM appointments);

-- 39. Find bills greater than average bill amount.
SELECT * FROM bills 
WHERE total_amount > (SELECT AVG(total_amount) FROM bills);

-- 40. Find patient with highest bill amount.
SELECT * FROM patients 
WHERE patient_id = (SELECT patient_id FROM bills ORDER BY total_amount DESC LIMIT 1);

-- 41. Find doctors whose consultation fee is above average.
SELECT * FROM doctors 
WHERE consultation_fee > (SELECT AVG(consultation_fee) FROM doctors);

-- 42. Find patients who visited Cardiology.
SELECT * FROM patients 
WHERE patient_id IN (
    SELECT DISTINCT patient_id FROM appointments WHERE doctor_id IN (
        SELECT doctor_id FROM doctors WHERE department_id = (
            SELECT department_id FROM departments WHERE department_name = 'Cardiology'
        )
    )
);

-- 43. Find unpaid bills.
SELECT * FROM bills WHERE bill_status = 'Unpaid';

-- 44. Find appointments that have treatments.
SELECT * FROM appointments 
WHERE appointment_id IN (SELECT DISTINCT appointment_id FROM treatments);

-- 45. Find patients whose total bill is above average patient billing.
SELECT p.*, SUM(b.total_amount) as patient_total_billing 
FROM patients p
JOIN bills b ON p.patient_id = b.patient_id
GROUP BY p.patient_id
HAVING SUM(b.total_amount) > (
    SELECT AVG(sub.total_per_patient) FROM (
        SELECT SUM(total_amount) as total_per_patient FROM bills GROUP BY patient_id
    ) sub
);

-- PART-6:Data Quality Checks 

-- 46. Find appointments without treatment.
SELECT * FROM appointments 
WHERE appointment_id NOT IN (SELECT DISTINCT appointment_id FROM treatments);

-- 47. Find bills without payment.
SELECT * FROM bills 
WHERE bill_id NOT IN (SELECT DISTINCT bill_id FROM payments);

-- 48. Find payments with NULL or zero paid amount.
SELECT * FROM payments WHERE paid_amount IS NULL OR paid_amount = 0;

-- 49. Find cancelled appointments that still have bills.
SELECT b.*, a.appointment_status 
FROM bills b
JOIN appointments a ON b.appointment_id = a.appointment_id
WHERE a.appointment_status = 'Cancelled';

-- 50. Find paid bills where payment amount is less than bill amount.
SELECT b.bill_id, b.total_amount, SUM(p.paid_amount) AS total_paid
FROM bills b
JOIN payments p ON b.bill_id = p.bill_id
WHERE p.payment_status = 'Success'
GROUP BY b.bill_id, b.total_amount
HAVING total_paid < b.total_amount;

-- 51. Find doctors with invalid department ID.
SELECT * FROM doctors 
WHERE department_id NOT IN (SELECT department_id FROM departments);

-- 52. Find appointments with invalid patient or doctor IDs.
SELECT * FROM appointments 
WHERE patient_id NOT IN (SELECT patient_id FROM patients)
   OR doctor_id NOT IN (SELECT doctor_id FROM doctors);

-- Final Management Report

-- Report 1: Patient Billing Report
SELECT 
    p.patient_name AS `Patient Name`,
    p.city AS `City`,
    COUNT(DISTINCT a.appointment_id) AS `Total Appointments`,
    COALESCE(SUM(DISTINCT b.total_amount), 0) AS `Total Bill Amount`,
    COALESCE(SUM(CASE WHEN pay.payment_status = 'Success' THEN pay.paid_amount ELSE 0 END), 0) AS `Total Paid Amount`,
    (COALESCE(SUM(DISTINCT b.total_amount), 0) - COALESCE(SUM(CASE WHEN pay.payment_status = 'Success' THEN pay.paid_amount ELSE 0 END), 0)) AS `Pending Amount`
FROM patients p
LEFT JOIN appointments a ON p.patient_id = a.patient_id
LEFT JOIN bills b ON a.appointment_id = b.appointment_id
LEFT JOIN payments pay ON b.bill_id = pay.bill_id
GROUP BY p.patient_id, p.patient_name, p.city
ORDER BY `Pending Amount` DESC;






     
