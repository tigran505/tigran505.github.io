---
modified: 2025-04-05T10:07:24+07:00
created: 2025-02-21T11:41:04+07:00
tags: Программирование
publish: true
---
- [[Кортежи Python]]
```python
import mysql.connector  
  
mydb = mysql.connector.connect (  
    host= "localhost" ,  
    port= "8889",  
    user= "root",  
    password= "root",  
    database = "python-example"  
)  
  
myCur = mydb.cursor()  
  
# sql = "CREATE DATABASE `python-example`" # Создаём базу данных, которая называется python-examples  
# sql = "SHOW DATABASES" # Показываем все датабазы  
# sql = "CREATE TABLE users (name VARCHAR(255), age INTEGER(3))" # Создаём таблицу  
# sql = "SHOW TABLES" # Показываем все таблички в датабазе  
sql = "INSERT INTO example (title, intro, date) VALUES (%s, %s, %s)"  
articles = [  
    (  
    'Третья статья',  
    'Spaghetti text',  
    '2025-02-20'  
    ),  
    (  
    'Четвёртая статья',  
    'Here we go text',  
    '2025-02-21'  
    )  
]  
# myCur.execute(sql, article) # Для одного запроса  
myCur.executemany(sql, articles) # Для двух и более запросов
mydb.commit
```
## Работаем с уже добавленными данными
- Также можно объединять условия через AND (И), OR (ИЛИ)
- Можно сортировать (ORDER BY *столбец*) по убыванию (DESC)
- Можно ограничить количество записей (LIMIT *число*) и пропустить (OFFSET *число*)
```python
import mysql.connector  
  
mydb = mysql.connector.connect (  
    host= "localhost" ,  
    port= "8889",  
    user= "root",  
    password= "root",  
    database = "python-example"  
)  
  
myCur = mydb.cursor()  
# sql = "SELECT id FROM example" # Выбираем только данные из столбца id для таблички example  
# sql = "SELECT * FROM example WHERE title <> 'Первая статья'" # Выбираем данные для таблички example, где заголовок title не равен значению 'Первая статья'  
# sql = "SELECT * FROM example WHERE title LIKE "%статья%" # Выбираем данные для таблички example, где заголовок title будет похож на "статья". При этом нам не важно, что будет до или после этого  
sql = "SELECT * FROM example" # Выбираем ВСЕ данные для таблички example  
myCur.execute(sql)  
  
result = myCur.fetchall()  
for element in result:  
    print(element)
```
## Обновление данных
```python
import mysql.connector  
  
mydb = mysql.connector.connect (  
    host= "localhost" ,  
    port= "8889",  
    user= "root",  
    password= "root",  
    database = "python-example"  
)  
  
myCur = mydb.cursor()  
sql = "UPDATE example SET title = %s WHERE id = %s"  
myCur.execute(sql, ("Обновлённый заголовок третьей статьи", 3))  
mydb.commit()
```
## Удаление данных
```python
import mysql.connector  
  
mydb = mysql.connector.connect (  
    host= "localhost" ,  
    port= "8889",  
    user= "root",  
    password= "root",  
    database = "python-example"  
)  
  
myCur = mydb.cursor()  
sql = "DELETE FROM example WHERE title = %s"  
myCur.execute(sql,("Обновлённый заголовок третьей статьи"))  
mydb.commit()
```
### Удаление вообще всех данных
```python
import mysql.connector  
  
mydb = mysql.connector.connect (  
    host= "localhost" ,  
    port= "8889",  
    user= "root",  
    password= "root",  
    database = "python-example"  
)  
  
myCur = mydb.cursor()  
sql = "DELETE FROM example"  
myCur.execute(sql)  
mydb.commit()
```
### Удаление вообще всей таблицы
```python
import mysql.connector  
  
mydb = mysql.connector.connect (  
    host= "localhost" ,  
    port= "8889",  
    user= "root",  
    password= "root",  
    database = "python-example"  
)  
  
myCur = mydb.cursor()  
sql = "DROP TABLE example"  
myCur.execute(sql)  
mydb.commit()
```