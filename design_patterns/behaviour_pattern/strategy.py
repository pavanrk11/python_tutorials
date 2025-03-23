# Strategy design pattern

# Take a class that does something specific in a lot of different ways
# extract all of these algorithms into separate classes called strategies

# Context :
# Strategy :
# Concrete Strategy :
# Client :

from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


class BubbleSortStrategy(SortStrategy):

    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


class QuickSortStrategy(SortStrategy):

    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)


class MergeSortStrategy(SortStrategy):

    def sort(self, data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)


# Client code
def client_code(data, context):
    print(context.sort(data))


if __name__ == "__main__":
    # data
    data = [5, 2, 9, 1, 5, 6]

    # Using BubbleSortStrategy
    bubble_sort = BubbleSortStrategy()
    context = Context(bubble_sort)
    client_code(data, context)

    # Using QuickSortStrategy
    quick_sort = QuickSortStrategy()
    context.set_strategy(quick_sort)
    client_code(data, context)

    # Using MergeSortStrategy
    merge_sort = MergeSortStrategy()
    context.set_strategy(merge_sort)
    client_code(data, context)
