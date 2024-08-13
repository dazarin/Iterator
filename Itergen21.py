class FlatIterator:

    def __init__(self, list_of_list):
        self.lists = list_of_list
        self.i = 0
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.lists):
            if self.j < len(self.lists[self.i]):
                item = self.lists[self.i][self.j]
                self.j += 1
                return item
            self.j = 0
            self.i += 1
        raise StopIteration

test_lst = [['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None]]
iterator = FlatIterator(test_lst)
for item in iterator:
    print(item, end=' ')

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()