class DynamicArray:
    # my_array = [4]
    def _init_(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity

        def insert(self, index, value):
            # 2nd- make sure we have open space
            if self.count >= self.capacity:
                print("error: array is full")
                return
            # 3rd- make sure index is in range
            if index >= self.count:
                print("error out of range")
                return

            # shift everything over

            # 1st- insert out value
            self.storage[index] = value
            self.count += 1