---
{"tags":["Программирование"],"publish":true,"modified":["2025-04-04T15:42:30+07:00"],"created":"2024-12-16T19:11:14.000+07:00","PassFrontmatter":true,"updated":"2025-04-12T12:12:09.941+07:00"}
---

- Упорядоченные коллекции элементов одного типа
- Позволяют хранить несколько значений в одной [[Сферы/Программирование/Swift/Переменные Swift\|Переменная]] или [[Сферы/Программирование/Swift/Константы Swift\|Константа]] 
1. Строго типизрованы (нельзя смешивать типы данных в одном массиве)
2. Иммутабельны (если массив объявлён с помощью let, его нельзя изменять)
## Пустой массив
```swift
var emptyArray: [int] = [ ] 
```
## Массив с начальными значениями
```swift
let numbers = [1, 2, 3, 4, 5]
```
## Массив с повторяющимися значениями
```swift
let repeatedArray = Array(repeating: 0, count 5)
```
## Основные операции с массивами
### Добавление элементов
```swift
var array = [1, 2. 3]
array.append(4)
array += [5, 6]
```
### Изменение элементов
```swift
var array = [10, 20, 30]
array[0] = 15 // [15, 20, 3]
```
### Удаление элементов
```swift
var array = [1, 2, 3, 4]
array.remove(at: 2)
array.removeLast()
array.removeAll()
```
### Доступ к элементам
```swift
let firstElement = array[0] // Доступ к первому элементу
let count = array.count // Количество элементов
```
### Проверка на пустоту
```swift
if array.isEmpty {
	print("Массив пуст")
}
```
## Перебор массива с помощью [[Сферы/Программирование/Swift/Циклы в Swift\|Циклы в Swift]]
### Цикл for
```swift
let numbers = [1, 2, 3]
for numbers in numbers {
	print(number)
}
```
### С доступом к индексам
```swift
for (index, value) in numbers.enumerated() {
	print("index \(index): \(value)")
}
```
## Методы массивов
### contains
- Проверяет наличие элемента в массиве
```swift
let numbers = [1, 2, 3]
let hasThree = numbers.contains(3)
```
### first и last
- Возвращают первый и последний элемент
```swift
let numbers = [1, 2, 3]
let first = numbers.first // 1
let last = numbers.last // 3

```
### sorted
- Возвращает отсортированный массив
```swift
let numbers = [3, 1, 2]
let sortedArray = numbers.sorted()
print(sortedArray)
```
### map
- Преобразует элементы массива
```swift
let numbers = [1, 2, 3]
let doubled = numbers.map { $0 * 2 } 
print(doubled)
```
### filter
```swift
let numbers = [1, 2, 3]
let filtered = numbers.filter { $0 > 2 }
print(filtered) // 3
```