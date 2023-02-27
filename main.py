class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        self._cache = {}
        self.capacity = capacity

    def __len__(self):
        return len(self._cache);

    def __str__(self):
        return str(self._cache);

    def get(self, key: str) -> str:
        value = self._cache.pop(key)
        self._cache[key] = value
        return value;

    def set(self, key: str, value: str) -> None:
        self._cache.pop(key, None)
        if len(self) < self.capacity:
            self._cache[key] = value
        else:
            del self._cache[next(iter(self._cache.keys()))]
            self._cache[key] = value

    def rem(self, key: str) -> None:
        del self._cache[key]

lru = LRUCache(10)
lru.set('a', '0')
lru.set('b', '1')
lru.set('c', '2')
lru.set('d', '3')
lru.set('e', '4')
lru.set('f', '5')
lru.set('g', '6')
lru.set('h', '7')
lru.set('i', '8')
lru.set('j', '9')

print(f'Начальные значения: {lru}\nРазмер: {len(lru)}\n')

lru.set('k', '10')
print(f'Добавление элемента с новым ключем \'k\': {lru}\nРазмер: {len(lru)}\n')

lru.set('d', '34')
print(f'Изменение значения существующего ключа \'d\': {lru}\nРазмер: {len(lru)}\n')

lru.rem('i')
print(f'Удаление ключа \'i\': {lru}\nРазмер: {len(lru)}\n')

lru.set('y', '99')
lru.set('z', '100')
print(f'Добавление двух новых ключей \'y\' и \'z\': {lru}\nРазмер: {len(lru)}')