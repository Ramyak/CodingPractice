get_left = lambda i: (2 * i) + 1
get_right = lambda i: (2 * i) + 2
get_parent = lambda i: (i - 1) / 2

class Heap(object):
    def __init__(self, is_min = True):
        self.arr = []
        self.is_min = is_min

    def compare(self, small, big):
        if self.is_min and self.arr[small] < self.arr[big]:
            return True
        if not self.is_min and self.arr[small] > self.arr[big]:
            return True
        return False

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
    
    def move(self, x, y):
        self.arr[y] = self.arr[x]
        del self.arr[x]

    def bubble_up(self, i):
        # bubble up #
        while i != 0:
            parent = get_parent(i)
            if self.compare(small = parent, big = i):
                break
            self.swap(i, parent)
            i = parent
        return i

    def bubble_down(self, i):
        while True:
            left = get_left(i)
            if left >= len(self.arr):
                break
            right = get_right(i)
            # Min value of left and right
            change = left
            if right < len(self.arr) and self.compare(small = right, big = left):
                change = right
            if self.compare(small = i, big = change):
                break
            self.swap(i, change)
            i = change

    def add(self, x):
        self.arr.append(x)
        i = len(self.arr) - 1
        return self.bubble_up(i)

    def get(self):
        if len(self.arr) == 0:
            return None
        return_value = self.arr[0]
        self.move(len(self.arr) - 1, 0)
        self.bubble_down(0)
        return return_value

    def del_node(self, i):
        self.move(len(self.arr) - 1, i)
        if i >= len(self.arr):
            return
        if i != 0:
            parent = get_parent(i)
            if not self.compare(small = parent, big = i):
                self.bubble_up(i)
                return
        right = get_right(i)
        left = get_left(i)
        if (left < len(self.arr) and not self.compare(small = i, big = left)) \
                or (right < len(self.arr) and not self.compare(small = i, big = left)):
                        self.bubble_down(i)
