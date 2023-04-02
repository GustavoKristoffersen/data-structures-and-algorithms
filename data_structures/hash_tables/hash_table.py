class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size
        
    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash += ord(key[i]) * i
        return hash % self.size

    def set(self, key, value):
        address = self._hash(key)
        if self.data[address] is None:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self._hash(key)
        bucket = self.data[address]
        if bucket:
            for k, v in bucket:
                if k == key:
                    return v
        return None
    
    def delete(self, key):
        address = self._hash(key)
        bucket = self.data[address]
        if bucket:
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    del bucket[i]
                    return True
        return False

    def keys(self):
        keys = []
        for i in range(len(self.data)):
            bucket = self.data[i]
            if bucket:
                for j in range(len(bucket)):
                    keys.append(bucket[j][0])
        return keys
