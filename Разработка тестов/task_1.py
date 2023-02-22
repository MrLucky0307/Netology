import lesson_4
import unittest


class TestHomework(unittest.TestCase):
    def test_task_1(self):
        self.assertEqual(lesson_4.sort_list(), [
            {'visit1': ['Москва', 'Россия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ])

    def test_task_2(self):
        self.assertEqual(lesson_4.get_unique_id(), [98, 35, 15, 213, 54, 119])

    def test_task_4(self):
        self.assertEqual(lesson_4.max_stats_chanel(), 'yandex')


if __name__ == "main":
    unittest.main()
