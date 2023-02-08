import os


def logger(old_function):
    def new_function(*args, **kwargs):
        import datetime
        f = open('task_3.log', 'a')
        f.write(f'{datetime.datetime.now()}\n')
        f.write(f'{str(old_function.__name__)}\n')
        for value_args in args:
            f.write(f'{value_args}\n')
        for value_kwargs in kwargs.values():
            f.write(f'{value_kwargs}\n')
        return_value = old_function(*args, **kwargs)
        f.write(str(return_value) + "\n")
        f.close()
        return return_value

    return new_function


def main():
    path = 'task_3.log'
    if os.path.exists(path):
        os.remove(path)

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    @logger
    def flat_generator(list_of_lists):
        for list_ in list_of_lists_1:
            for item in list_:
                yield item
    flat_generator(list_of_lists_1)


if __name__ == "__main__":
    main()
