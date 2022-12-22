USE Airport
--Вывести все рейсы в определенный город на произвольную дату, упорядочив их по времени вылета;

--SELECT *
--FROM Flights 
--JOIN Destinations ON Flights.id_destination = Destinations.id_destination
--WHERE Destinations.to_city = 'Омск' AND YEAR(departure_dt) BETWEEN '2020' AND '2021'
--ORDER BY departure_dt;

--Вывести информацию о рейсе с наибольшей длительностью полета по времени;

--SELECT from_city, to_city, departure_dt, arrival_dt, plane, DATEDIFF(HOUR, departure_dt, arrival_dt) AS [Difference]
--FROM Flights
--JOIN Destinations ON Flights.id_destination = Destinations.id_destination
--JOIN Planes ON Flights.id_plane = Planes.id_plane
--WHERE DATEDIFF(HOUR, departure_dt, arrival_dt) = (
--	SELECT MAX(DATEDIFF(HOUR, departure_dt, arrival_dt))
--	FROM Flights);

--Показать все рейсы, длительность полета которых превышает два часа;
--Т.к. самые короткие рейсы в таблице равны 4 часам, то вывел те, что больше 6 часов.

--SELECT from_city, to_city, plane, departure_dt, arrival_dt,
--DATEDIFF(HOUR, departure_dt, arrival_dt) AS [Difference],
--seats_in_economy, seats_in_business
--FROM Flights
--JOIN Destinations ON Flights.id_destination = Destinations.id_destination
--JOIN Planes ON Flights.id_plane = Planes.id_plane
--WHERE DATEDIFF(HOUR, departure_dt, arrival_dt) > 6;

--Получить количество рейсов в каждый город

--SELECT to_city, COUNT(*) as [Number_of_flights]
--FROM Destinations, Flights
--WHERE Flights.id_destination = Destinations.id_destination
--GROUP BY to_city;

--Показать город, в который наиболее часто осуществляются полеты;

--SELECT TOP 1 to_city, COUNT(*) as [Number_of_flights]
--FROM Destinations, Flights
--WHERE Flights.id_destination = Destinations.id_destination
--GROUP BY to_city
--ORDER BY Number_of_flights DESC;

--Получить информацию о количестве рейсов в каждый город и общее количество рейсов за определенный месяц;

--SELECT to_city, COUNT(*) as [Number_of_flights]
--FROM Destinations, Flights
--WHERE Flights.id_destination = Destinations.id_destination AND YEAR(departure_dt) = 2021 AND MONTH(departure_dt) = 4
--GROUP BY to_city
--UNION ALL
--SELECT 'Общее кол-во вылетов' AS to_city, COUNT(*) as [Number_of_flights]
--FROM Destinations, Flights
--WHERE Flights.id_destination = Destinations.id_destination AND YEAR(departure_dt) = 2021 AND MONTH(departure_dt) = 4

--Получить информацию о количестве проданных билетов на все рейсы за указанный день и их общую сумму

--SELECT departure_dt, COUNT(*) AS [Number_of_tickets], SUM(price) AS [Total_sum]
--FROM Tickets
--JOIN Flights ON Tickets.flight = Flights.id_flight
--WHERE YEAR(departure_dt) = 2021 AND MONTH(departure_dt) = 1 AND DAY(departure_dt) = 24
--GROUP BY departure_dt;

--Вывести список рейсов, вылетающих сегодня, на которые есть свободные места в бизнес классе

SELECT plane, departure_dt, arrival_dt, seats_in_business, seats_in_business - COUNT(Tickets.class) AS [Free_seats_in_business]
FROM Tickets
JOIN Flights ON Tickets.flight = Flights.id_flight
JOIN Planes ON  Flights.id_plane = Planes.id_plane
WHERE YEAR(departure_dt) = 2020 AND MONTH(departure_dt) = 11 AND DAY(departure_dt) = 22 AND Tickets.class = 'Business'
GROUP BY plane, departure_dt, arrival_dt, seats_in_business;
