# Write your MySQL query statement below
SELECT student_id, student_name, subject_name, COUNT(exam.student_id) AS attended_exams
FROM Students
JOIN Subjects
LEFT JOIN Examinations AS exam USING(student_id, subject_name)
GROUP BY student_id, subject_name
ORDER BY student_id, subject_name
