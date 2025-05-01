---
tags: Программирование
publish: true
modified:
  - 2025-05-01T12:50:30+07:00
created: 2025-02-20T15:39:17+07:00
---
## Условие
- Нужно сделать игру "Камень, ножницы, бумага"
1. Нужно создать перечисления
2. Нужно создать класс Player, внутри которого должен быть конструктор, который принимает 2 параметра 
	1. Эти 2 параметра должны иметь значения по умолчанию 
3. Нужно создать метод whoWins, в который будут передаваться два объекта "bot" и "alex"
```python
# ФАЙЛ main.py
# Импорт файлов и классов из них  
from player import Player  
from variants import Variants  
  
# Создаем объекты на основе класса Player  
bot = Player ()
  
# При создании можем не передавать значения или же  
# можем передать выбор (камень, ножницы или бумага), а также имя  
alex = Player (Variants.SCISSORS, "ALex")  
  
# далее через объект можем обратить к функции whoWins  
# и мы узнаем кто победил  
print (bot.whoWins(bot, alex))
```
## Решение 
0. Пришлось чуть-чуть **модифицировать файл main.py**, так как я накосячил с названием переменной (SCISSOR вместо SCISSORS), а также нечаянно избавился от значения "bot", передавая его изначально как self. При этом условие самого задания не было нарушено, так что **всё с кайфом**
1. Файл variants.py был реализован через создание [[Перечисления|перечисления]] с тремя вариантами: камнем, ножницами и бумагой 
2. В файл player.py был импортирован класс Variants из файла variants.py
3. Затем был создан класс Player, в котором был создан конструктор с объектом self, choice (сам выбор) и name 
4. После этого был создан метод whoWins, который определяет, кто выиграл, а кто проиграл, исходя из значений основного файла
	1. Важно использовать return, а не print, так как используя [[Оператор print]] будет добавляться лишняя строка "None", и это не есть красиво
### main.py
```python
# Файл main.py  
# Импорт файлов и классов из них  
from player import Player  
from variants import Variants  
 
bot = Player () # По умолчанию задан Variants.ROCK, но можно добавить в скобки Variants.PAPER или Variants.SCISSOR для бумаги и ножниц соответственно 

player = Player () # По умолчанию задан Variants.ROCK, как и для bot, но можно добавить в скобки Variants.PAPER или Variants.SCISSOR для бумаги и ножниц соответственно   

print (bot.whoWins(player)) # Выводим результат игры 
```
### variants.py
```python
# Файл variants.py  
from enum import Enum  
  
class Variants(Enum):  
    ROCK = "Камень",  
    PAPER = "Ножницы",  
    SCISSOR = "Бумага"
```
### player.py
```python
# Файл player.py  
from variants import Variants  
  
class Player:  
   def __init__(self, choice=Variants.ROCK, name="bot"):  
       self.choice = choice  
       self.name = name  
  
   def whoWins(self, player):  
       if self.choice == player.choice:  
           return "У игроков player и bot ничья"  
       if self.choice == Variants.ROCK and player.choice == Variants.PAPER:  
            return "Игрок player победил игрока bot, так как бумага бьёт камень"  
       if self.choice == Variants.PAPER and player.choice == Variants.ROCK:  
           return "Игрок bot победил игрока player, так как бумага бьёт камень"  
       if self.choice == Variants.PAPER and player.choice == Variants.SCISSOR:  
           return "Игрок player победил игрока bot, так как ножницы бьют бумагу"  
       if self.choice == Variants.SCISSOR and player.choice == Variants.PAPER:  
           return "Игрок bot победил игрока player, так как ножницы бьют бумагу"  
       if self.choice == Variants.SCISSOR and player.choice == Variants.ROCK:  
           return "Игрок player победил игрока bot, так как камень бьёт ножницы"  
       if self.choice == Variants.ROCK and player.choice == Variants.SCISSOR:  
           return "Игрок bot победил игрока player, так как камень бьёт ножницы"
``` 