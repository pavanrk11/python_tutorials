class Iterator:
    def __iter__(self):
        raise NotImplementedError

    def __next__(self):
        raise NotImplementedError


class MyIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value


class Collection:

    def create_iterator(self):
        raise NotImplementedError


class MyCollection(Collection):

    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def create_iterator(self):
        return MyIterator(self.data)


def main():

    my_collection = MyCollection()
    my_collection.add(1)
    my_collection.add(2)
    my_collection.add(3)

    # Creating an iterator for the collection
    my_iterator = my_collection.create_iterator()

    # Using the iterator to traverse through the elements
    for element in my_iterator:
        print(element)


if __name__ == "__main__":
    main()