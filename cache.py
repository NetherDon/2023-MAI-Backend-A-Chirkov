class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        self._cache = {}
        self.capacity = capacity

    def __len__(self):
        return len(self._cache)

    def __str__(self):
        return str(self._cache)

    def get(self, key: str) -> str:
        value = self._cache.pop(key, None)
        if value is not None:
            self._cache[key] = value
        return value or ""

    def set(self, key: str, value: str) -> None:
        self._cache.pop(key, None)
        if len(self) < self.capacity:
            self._cache[key] = value
        else:
            del self._cache[next(iter(self._cache.keys()))]
            self._cache[key] = value

    def rem(self, key: str) -> None:
        del self._cache[key]
