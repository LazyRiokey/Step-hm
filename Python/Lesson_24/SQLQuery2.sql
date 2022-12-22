USE Airport
SELECT *
FROM Flights, Destinations
WHERE Flights.id_destination = Destinations.id_destination AND to_city = 'Уфа'
ORDER BY departure_dt;