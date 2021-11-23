--Выбираем столбец classroom из таблицы Schedule- расписание занятий
SELECT classroom 
FROM Schedule
--Выбираем кабинеты с самым большим спросом
GROUP BY classroom
HAVING COUNT(classroom) = 
    (SELECT COUNT(classroom) 
     FROM Schedule 
     GROUP BY classroom
     ORDER BY COUNT(classroom) DESC 
     LIMIT 1)