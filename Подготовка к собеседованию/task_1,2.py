class Stack:
    def __init__(self, sequence):
        self.sequence = sequence
        self.list = []
        self.balance_list = []
        for item in sequence:
            self.list.append(item)
        self.pairs = {"{": "}", "(": ")", "[": "]"}

    # Проверка стека на пустоту
    def is_empty(self):
        return len(self.list) == 0

    # Добавляет новый элемент на вершину стека
    def push(self, el):
        self.list.append(el)

    # Удаляет верхний элемент стека, возвращает верхний элемент стека
    def pop(self):
        delete_last_el = self.list.pop()
        return delete_last_el

    # Возвращает верхний элемент стека, но не удаляет его
    def peek(self):
        return self.list[-1]

    # Возвращает количество элементов в стеке
    def size(self):
        return len(self.list)

    # Проверка сбалансированности последовательности
    def check_balance(self):
        for item in self.sequence:
            if item in "{([":
                self.balance_list.append(item)
            elif self.balance_list and item == self.pairs[self.balance_list[-1]]:
                self.balance_list.pop()
            else:
                return "Несбалансировано"
        return "Сбалансировано"


if __name__ == "__main__":
    test_sequence = input("Введите последовательность: ")
    if len(test_sequence) == 0:
        print("Вы ничего не ввели!")
    else:
        test = Stack(test_sequence)
        print(test.check_balance())
