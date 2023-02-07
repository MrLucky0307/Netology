class FlatIterator:

    def __init__(self, list_of_list):
        def flat_iterator(lst, res=[]):
            for item in lst:
                if isinstance(item, list):
                    flat_iterator(item)
                else:
                    res.append(item)
            return res
        self.list = flat_iterator(list_of_list)
        self.start = -1
        self.end = len(self.list)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        for item in self.list:
            self.list.remove(item)
            return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
