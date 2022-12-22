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

/* USE University
SELECT Department, COUNT(Teachers.Teacher_id) AS [Number of teachers]
FROM Department, Teachers
WHERE Department.Department_id = Teachers.Department_id
GROUP BY Department; */

-- Запрос 15

/* USE University
SELECT [Group].Group_number, COUNT(Students.id) AS [Number of students], Students.[Grant] AS [Grant]
FROM Students, [Group]
WHERE Students.Group_id = [Group].Group_id
GROUP BY [Group].Group_number, [Grant]; */

-- Запрос 16

/* USE University
SELECT [First name], [Last name], [Grant]
FROM Students
GROUP BY [First name], [Last name], [Grant]
HAVING [Grant] <= 8000
ORDER BY [Grant]; */

-- Запрос 17

/* USE University
SELECT [Group].Group_number, COUNT(*) AS [Number of Students]
FROM [Group], Students
WHERE [Group].Group_id = Students.Group_id
GROUP BY [Group].Group_number
HAVING COUNT(Students.Group_id) > 5; */

-- Запрос 18

/* USE University
SELECT Department.Department, COUNT(*) AS [Number of Teachers]
FROM Teachers, Department
WHERE Department.Department_id = Teachers.Department_id
GROUP BY Department
HAVING COUNT(Teachers.Teacher_id) < 4; */

-- Запрос 19

/* SELECT [First name], [Last name], Group_number, [Grant]
FROM Students, [Group]
WHERE [Group].Group_id = Students.Group_id
GROUP BY [First name], [Last name], Group_number, [Grant]
HAVING [Grant] = MAX([Grant]); */

-- Запрос 20

/* SELECT [First name], [Last name], Group_number, [Grant]
FROM Students, [Group]
WHERE [Group].Group_id = Students.Group_id AND [Grant] = (SELECT MAX([Grant]) FROM Students); */