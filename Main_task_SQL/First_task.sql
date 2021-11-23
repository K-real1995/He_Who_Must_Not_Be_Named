--Производим выборку из имен таблицы Passenger
SELECT name, COUNT(*) AS count  
FROM Passenger
--Соединяя с таблицей Pass_in_trip, 
JOIN Pass_in_trip
    ON Passenger.id=Pass_in_trip.passenger
--Отсортировываем по количеству перелетов и имени пассажиров 
GROUP BY passenger
--Сортировка пассажиров с количеством полетов от 1
HAVING COUNT(trip) > 0
ORDER BY COUNT(trip) DESC, name;