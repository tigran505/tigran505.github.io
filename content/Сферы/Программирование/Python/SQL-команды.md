---
tags: Программирование
publish: true
modified:
  - 2025-04-06T11:16:54+07:00
created: 2025-02-21T14:32:27+07:00
---
## Конфликты
```MySQL
CREATE DATABASE `sql` # Создаём базу данных с именем sql

INSERT INTO `my_byers`(`age`, `name`, `price`) VALUES (30, 'Bob', 450), (20, 'Steve', 500), (13, 'Rob', 50), (43, 'Jane', 300) # Ничего необычного, просто добавляем данные в поля таблички my_byers

INSERT INTO `my_byers`(`id`, `age`, `name`, `price`) VALUES (2, 43, 'Diana', 444) ON DUPLICATE KEY UPDATE `age` = 43 # ON - обработчик конфликта, DUPLICATE - сам конфликт
``` 
## Аналогичный запрос для конфликта в [[PostgreSQL]]
```PostgreSQL
INSERT INTO my_byers(id, age, name, price) VALUES (2, 43, 'Diana', 444) ON CONFLICT(id) DO UPDATE SET age = 43
```
## Внешние ключи
```MySQL
CREATE TABLE parent ( id INT NOT NULL, PRIMARY KEY(id)) ENGINE=INNODB # Создаём таблицу parent на движке INNODB, а не на MyISAM, так как вторая не поддерживает ссылки на данные из других таблиц

CREATE TABLE сhild ( # Создаём таблицу child 
 	id INT NOT NULL,
    parent_id INT, 
	PRIMARY KEY(id), # id должен быть уникальным
    FOREIGN KEY (parent_id) # Создаём родительское поле
    	REFERENCES parent(id) # Ссылаемся на значение id из таблички parent
    	ON DELETE CASCADE # Обрабатываем конфликт: если id будет удалён, то и parent_id будет удалён
) ENGINE=INNODB

INSERT INTO `parent`(`id`) VALUES (1), (2), (3) # Добавляем записи в parent в поле id
```
### Практика 
```MySQL
CREATE TABLE users ( # Создаём табличку users, где мы будем хранить информацию о покупателях 
	id INT (11) NOT NULL AUTO_INCREMENT,
	age INT(5) NOT NULL,
	name VARCHAR(50) NOT NULL,
	PRIMARY KEY (id) # id должен быть уникальным
) ENGINE=INNODB # По умолчанию и так ставится InnoDB, но лучше дополнительно указать 

INSERT INTO `users`(`age`, `name`) VALUES (16, 'Tigran'), (47, 'Ki Hun'), (42, 'Sang Woo'), (25, 'Sae Byeok'), (26, 'Jimmy') # Добавляем данные в табличку users для полей age и name (создаём покупателей)

CREATE TABLE items ( # Создаём табличку items, где мы будем хранить информацию о товарах
	id INT (11) NOT NULL AUTO_INCREMENT,
	price INT(5) NOT NULL,
	name VARCHAR(50) NOT NULL,
	PRIMARY KEY (id)
) ENGINE=INNODB

INSERT INTO `items`(`price`, `name`) VALUES (999, 'iPhone'), (299, 'iPad'), (49, 'iPod Shuffle'), (149, 'Apple TV'), (10, 'EarPodes') # Добавляем данные в табличку items для полей price и name (создаём товары)

CREATE TABLE orders (  # Создаём табличку orders, где мы будем хранить информацию о заказах
	id INT (11) NOT NULL AUTO_ INCREMENT,
	userId INT(11) NOT NULL,
	itemId INT(11) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (userId) REFERENCES users(id), # userId ссылается на пользователя, который что-то купил
	FOREIGN KEY (itemId) REFERENCES items (id) # itemId ссылается на товар, который был куплен
) ENGINE=INNODB

INSERT INTO `orders` (`id`, `userId`, `itemId`) VALUES (NULL, '5', '1'), (NULL, '2', '5'); # Например, Jimmy купил iPhone, а  Ki Hun купил EarPodes

ALTER TABLE `items` ADD PRIMARY(`id`) # Добавление внешнего (первичного) ключа для таблицы items
ALTER TABLE `items` DROP PRIMARY(`id`) # Удаление внешнего (первичного) ключа для таблицы items
```
## Объединения
### Сырой вариант 1.0
- Прописываем команды в табличке orders
- Выводим все заказы и всех пользователей, которые осуществили эти заказы 
	- При этом выводится и всякий мусор в виде id обоих таблиц, а также userId и itemId
```MySQL
SELECT * FROM `orders`
JOIN `items` ON orders.itemId = items.id # Если id заказанного товара равен id обычного товара
JOIN `users` ON orders.userId = users.id; # Если id заказавшего пользователя равен id обычного пользователя
```
![[CleanShot 2025-02-21 at 13.51.25@2x.png|500]]
### Делаем красивее 2.0
```MySQL
SELECT users.name AS User, items.name AS Item FROM `orders` # Здесь сужаем выборку, оставляем только имена пользователей и имена товаров
JOIN `users` ON users.id = orders.userId
JOIN `items` ON items.id = orders.itemId
```
![[CleanShot 2025-02-21 at 14.03.59@2x.png|200]]
### Делаем и красиво, и полезно 3.0
```MySQL
SELECT users.name AS 'Имя покупателя', items.name AS 'Название товара', items.price AS 'Цена товара 'FROM `orders` # Добавлем отображение цены товара
JOIN `users` ON users.id = orders.userId
JOIN `items` ON items.id = orders.itemId
```
![[CleanShot 2025-02-21 at 14.14.50@2x.png|400]]
### Выводим общую сумму покупок 3.1
```MySQL
SELECT users.name AS 'Имя покупателя', SUM(items.price) AS 'Общая стоимость' FROM `orders`
JOIN `users` ON users.id = orders.userId
JOIN `items` ON items.id = orders.itemId
GROUP BY orders.userId
```
![[CleanShot 2025-02-21 at 14.22.20@2x.png|300]]
### Выводим покупателей, которые купили больше определённой суммы 3.2
```MySQl
SELECT users.name AS 'Имя покупателя', SUM(items.price) AS 'Общая стоимость' FROM `orders`
JOIN `users` ON users.id = orders.userId
JOIN `items` ON items.id = orders.itemId
GROUP BY orders.userId
HAVING SUM(items.price) > 100
```
![[CleanShot 2025-02-21 at 14.25.51@2x.png|300]]
### Итоговый вариант c максимальным юзабилити 4.0
```MySQL
SELECT CONCAT('Имя пользователя: ', users.name, ' . Общая стоимость: ', SUM(items.price)) AS 'Полная информация'
FROM `orders`
JOIN `users` ON users.id = orders.userId
JOIN `items` ON items.id = orders.itemId
GROUP BY orders.userId
HAVING SUM(items.price) > 100 
\```
![[CleanShot 2025-02-21 at 14.32.12@2x.png|400]]