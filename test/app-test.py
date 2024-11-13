import unittest
from app import app

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/hello')
        self.assertEqual(response.data.decode(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
