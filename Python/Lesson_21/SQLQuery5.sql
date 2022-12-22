-- Запрос 1

/* USE University
SELECT [First_name], [Last_name], Department
FROM Teachers, Department
WHERE Teachers.Department_id = Department.Department_id; */

-- Запрос 2

/* USE University
SELECT Teachers.First_name, Teachers.Last_name, Department.Department
FROM Teachers, Department
WHERE Teachers.Department_id = Department.Department_id
ORDER BY Department.Department; */

-- Запрос 3

/* USE University
SELECT AVG(Students.[Grant]) AS 'AVG-Grants'
FROM Students; */

-- Запрос 4

/* USE University
SELECT [First_name] + ' '  + [Last_name] AS 'Fullname', Department
FROM Teachers, Department
WHERE Teachers.Department_id = Department.Department_id; */

-- Запрос 5

/* USE University
SELECT COUNT(*) AS [Number of Records]
FROM Students; */

-- Запрос 6

/* USE University
SELECT COUNT([Grant]) AS [Number of Records]
FROM Students; */

-- Запрос 7

/* USE University
SELECT COUNT(DISTINCT [Grant]) AS [Number of Records]
FROM Students; */

-- Запрос 8

/* USE University
SELECT AVG(DATEDIFF(DD, Birthday, GETDATE()) / 365) AS [Average_age]
FROM Students; */

-- Запрос 9

/* USE University
SELECT SUM([Grant]) AS [Sum_of_grants]
FROM Students; */

-- Запрос 10

/* USE University
SELECT COUNT(*) AS [Count_of_students]
FROM Students
WHERE [First name] LIKE N'А%'; */

-- Запрос 11

/* USE University
SELECT COUNT(*) AS [Count_of_students]
FROM Students, [Group]
WHERE [Group_number] LIKE '%81' AND [Group].Group_id = Students.Group_id; */

-- Запрос 12

/* USE University
SELECT COUNT(*) AS [Count_of_teachers]
FROM Teachers, Department
WHERE Teachers.Department_id == 1 AND Teachers.Department_id = Department.Department_id; */

-- Запрос 13

/* USE University
SELECT *
FROM Students
WHERE [Grant] > (SELECT AVG([Grant]) FROM Students); */

-- Запрос 14

USE University
SELECT *
FROM Students
WHERE [Grant] > (SELECT AVG([Grant]) FROM Students);