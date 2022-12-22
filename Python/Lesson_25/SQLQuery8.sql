--Вывести список рейсов, вылетающих сегодня, на которые есть свободные места в бизнес классе

SELECT plane, departure_dt, arrival_dt, seats_in_business
FROM Tickets
JOIN Flights ON Tickets.flight = Flights.id_flight
JOIN Planes ON  Flights.id_plane = Planes.id_plane
WHERE YEAR(departure_dt) = 2021 AND MONTH(departure_dt) = 1 AND DAY(departure_dt) = 24;