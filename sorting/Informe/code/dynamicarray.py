class DynamicArray():
    m_size = 0
    m_data = []
    def __init__(self, m_size=0, data=[None]):
        self.m_size = m_size
        self.m_data = [data] * m_size
    def print(self):
        for i in range(0, self.m_size):
            print(f'{self.m_data[i] = }')
    def add(self, value):
        self.m_data.append(value)
        self.m_size += 1
    def remove(self):
        self.m_data.pop()
        self.m_data -= 1
    def size(self):
        return self.m_size
    def resize(self, n_size):
        if n_size == 0:
            while self.m_size >= 0:
                self.m_data.pop()
                self.m_size -= 1
        elif n_size > self.m_size:
            while n_size > self.m_size:
                self.m_data.append(None)
                self.m_size += 1
        else:
            tmp = DynamicArray(n_size)
            for i in range(tmp.size()):
                tmp.m_data[i] = self.m_data[i]
            del self.m_data
            self.m_data = tmp.m_data
            self.m_size = n_size
            del tmp
    def index(self, index):
        return self.m_data[index]
