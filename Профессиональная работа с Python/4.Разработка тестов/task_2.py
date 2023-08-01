import unittest
import yanAPI


class TestYanAPI(unittest.TestCase):
    def setUp(self):
        print('method setUp')

    def test_create_folder(self):
        self.assertEqual(yanAPI.create_folder("test"), 201)

    def test_code_409(self):
        self.assertNotEqual(yanAPI.create_folder("test"), 409)

    def tearDown(self):
        yanAPI.delete_folder('test')
        print('method tearDown')


if __name__ == "main":
    unittest.main()
