from cache import LRUCache

lru = LRUCache(10)
lru.set("a", "0")
lru.set("b", "1")
lru.set("c", "2")
lru.set("d", "3")
lru.set("e", "4")
lru.set("f", "5")
lru.set("g", "6")
lru.set("h", "7")
lru.set("i", "8")
lru.set("j", "9")

print(f'Начальные значения: {lru}\nРазмер: {len(lru)}\n')

print(f'Значение ключа \'g\': {lru.get("g")}')
print(f'Значение ключа \'d\': {lru.get("d")}')
print(f'Значение ключа \'z\': {lru.get("z")}')
print(f'Значения, после использования get: {lru}\nРазмер: {len(lru)}\n')

lru.set("k", "10")
print(f'Добавление элемента с новым ключем \'k\': {lru}\nРазмер: {len(lru)}\n')

lru.set("d", "34")
print(f'Изменение значения существующего ключа \'d\': {lru}\nРазмер: {len(lru)}\n')

lru.rem("i")
print(f'Удаление ключа \'i\': {lru}\nРазмер: {len(lru)}\n')

lru.set("y", "99")
lru.set("z", "100")
print(f'Добавление двух новых ключей \'y\' и \'z\': {lru}\nРазмер: {len(lru)}')