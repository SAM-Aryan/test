import unittest
from app import app

class HelloTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_without_name(self):
        response = self.app.get('/hello')
        self.assertEqual(response.data.decode(), "Hello, World!")
    
    def test_hello_with_name(self):
        response = self.app.get('/hello?name=John')
        self.assertEqual(response.data.decode(), "Hello, John!")

if __name__ == '__main__':
    unittest.main() 
