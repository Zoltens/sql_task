import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='user',
    password='password',
    database='test_task'
)
"""
первая задача на подсчет побед и поражений
"""
cur = dataBase.cursor()
sql_task_1 = "SELECT client_number, SUM(event_value.outcome = 'win') AS Побед, SUM(event_value.outcome = 'lose') AS " \
             "Поражений FROM bid INNER JOIN event_value ON bid.play_id = event_value.play_id AND bid.coefficient = " \
             "event_value.value GROUP BY client_number"
cur.execute(sql_task_1)
result = cur.fetchall()

for x in result:
    print(x)

"""
вторая задача на сортировку по кол-ву сыгранных матчей 
"""
sql_task_2 = "SELECT MAX(CONCAT(home_team,'-',away_team)) as game, COUNT(*) AS games_count " \
             "FROM event_entity GROUP BY least(home_team, away_team), greatest(home_team, away_team) ORDER BY count(*)"
cur.execute(sql_task_2)
result = cur.fetchall()

for x in result:
    print(x)

dataBase.close()
