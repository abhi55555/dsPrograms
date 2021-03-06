# implementing hash map using arrays(lists).


class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
            return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]

        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if key_hash is None:
            return False

        for i in range(len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

        return False

    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))


h = HashMap()
h.add('Bob', '345794567')
h.add('Ming', '340912784')
h.add('Ming', '324567890')
h.add('Alicia', '248515122')
h.add('Ankit', '987698760')
h.add('Aditya', '826428934')
h.add('Mike', '909099011')
h.add('Aditya', '486542199')
h.print()
h.delete('Alicia')
print('---------')
h.print()
print('---------')
print('Ming: ' + h.get('Ming'))
