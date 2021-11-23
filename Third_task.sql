--Выводим уникальные значения из таблицы Rooms
SELECT DISTINCT Rooms.*
FROM Rooms
--Объединяя с таблицей Reservations
JOIN Reservations
    ON Rooms.id=Reservations.room_id
--Где колонка 'start_date' в графе недели равна 12 и год равен 2020
WHERE WEEK(start_date, 1) = 12 AND YEAR(start_date)=2020;
