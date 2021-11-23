--Выбираем уникальные значения с применением фунции TIMEDIFF()
--Подсчитывающей разность между парами с id=2 до id=4 из таблицы 
--Timepair    
SELECT DISTINCT TIMEDIFF( 
                (SELECT end_pair FROM Timepair WHERE id=4),
                (SELECT start_pair FROM Timepair WHERE id=2)
                ) AS time
FROM Timepair;