-- Запрос 1

/* USE University
SELECT id, 
[First name] AS 'Имя', 
[Last name] AS 'Фамилия', 
[Birthday] AS 'Дата рождения'
FROM Students
WHERE MONTH(Birthday) = 2; */

-- Запрос 2 

/* USE University
SELECT *
FROM Students; */

-- Запрос 3

/* USE University
SELECT id,
[First name] + ' ' + [Last name] AS 'Имя Фамилия',
[Birthday] AS 'Дата рождения',
[Phone number] AS 'Номер телефона',
[Grant] AS 'Стипендия'
FROM Students; */

-- Запрос 4

/* USE University
SELECT id,
[First name] + ' ' + [Last name] + ' >> ' + CAST([Grant] AS nvarchar(10)) AS 'Информация'
FROM Students */

-- Запрос 5

/* USE University
SELECT id,
[First name] + ' ' + [Last name] AS 'Имя Фамилия',
[Birthday] AS 'Дата рождения',
[Phone number] AS 'Номер телефона',
[Grant] * 1.2 AS 'Стипендия'
FROM Students; */

-- Запрос 6

/* USE University
SELECT TOP 15 PERCENT id,
[First name] + ' ' + [Last name] AS 'Имя Фамилия',
[Birthday] AS 'Дата рождения',
[Phone number] AS 'Номер телефона',
[Grant] * 1.2 AS 'Стипендия'
FROM Students; */

-- Запрос 7

/* USE University
SELECT id,
[First name] AS 'Имя', 
[Last name] AS 'Фамилия',
[Birthday] AS 'Дата рождения',
[Phone number] AS 'Номер телефона',
[Grant] * 1.2 AS 'Стипендия'
FROM Students
WHERE [Grant] > 4000; */

-- Запрос 8

/* USE University
SELECT id,
[First name] AS 'Имя', 
[Last name] AS 'Фамилия',
[Birthday] AS 'Дата рождения',
[Phone number] AS 'Номер телефона',
[Grant] * 1.2 AS 'Стипендия'
FROM Students
WHERE LEN([First name]) < 8; */

-- Запрос 9

/* USE University
SELECT id,
[First name] AS 'Имя', 
[Last name] AS 'Фамилия',
[Birthday] AS 'Дата рождения',
[Phone number] AS 'Номер телефона',
[Grant] * 1.2 AS 'Стипендия'
FROM Students
WHERE MONTH([Birthday]) >= 9 AND MONTH([Birthday]) <= 11; */

-- Запрос 10

/* USE University
SELECT id,
[First name] AS 'Имя', 
[Last name] AS 'Фамилия',
[Birthday] AS 'Дата рождения',
[Phone number] AS 'Номер телефона',
[Grant] * 1.2 AS 'Стипендия'
FROM Students
WHERE YEAR([Birthday]) % 2 = 0 OR DAY([Birthday]) % 2 <> 0; */

-- Запрос 11

/* USE University
SELECT [First name] + ' ' + [Last name] AS 'ИНФО'
FROM Students
WHERE [Grant] > 5000; */

-- Запрос 12

/* USE University
SELECT id,
[First name] AS 'Имя', 
[Last name] AS 'Фамилия',
[Birthday] AS 'Дата рождения',
[Phone number] AS 'Номер телефона',
[Grant] AS 'Стипендия'
FROM Students
WHERE [Grant] BETWEEN 2000 AND 7000; */

-- Запрос 13

/* USE University
SELECT id,
[First name] AS 'Имя', 
[Last name] AS 'Фамилия',
[Birthday] AS 'Дата рождения',
[Phone number] AS 'Номер телефона',
[Grant] AS 'Стипендия'
FROM Students
ORDER BY [Grant] DESC; */

-- Запрос 14

/* USE University
SELECT id,
[First name] AS 'Имя', 
[Last name] AS 'Фамилия',
[Birthday] AS 'Дата рождения',
[Phone number] AS 'Номер телефона',
[Grant] AS 'Стипендия'
FROM Students
WHERE MONTH([Birthday]) BETWEEN 9 AND 11; */

-- Запрос 15

/* USE University
SELECT id,
[First name] AS 'Имя', 
[Last name] AS 'Фамилия'
FROM Students
WHERE LEN([First name]) BETWEEN 5 AND 8; */

-- Запрос 16

/*USE University
SELECT id,
[First name] AS 'Имя', 
[Last name] AS 'Фамилия',
[Birthday] AS 'Дата рождения',
[Phone number] AS 'Номер телефона',
[Grant] AS 'Стипендия'
FROM Students
WHERE [Last name] LIKE 'N[ЧА]%'; */

-- Запрос 17

/* USE University
SELECT id,
[First name] AS 'Имя', 
[Last name] AS 'Фамилия',
[Grant] AS 'Стипендия'
FROM Students
WHERE [Grant] * 1.5 < 10000; */

-- Запрос 18

/* USE University
SELECT id,
[First name] AS 'Имя', 
[Last name] AS 'Фамилия',
[Grant] AS 'Стипендия',
[Phone number] AS 'Номер телефона'
FROM Students
WHERE [Grant] * 1.5 < 10000 AND [Phone number] NOT LIKE '%2%'; */

-- Запрос 19

/* USE University
SELECT id,
[First name] AS 'Имя', 
[Last name] AS 'Фамилия',
[Grant] AS 'Стипендия',
[Phone number] AS 'Номер телефона'
FROM Students
WHERE [First name] IN (N'Арина'); */