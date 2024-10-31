import unittest
from Hello import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        #create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        #send a get request to the home route
        response = self.app.get('/')
        #check the status code

        self.assertEqual(response.status_code, 200)
      #check the response data
        self.assertEqual(response.json,{"message":"Hello level 400 FET, Quality Assurance!"})

if __name__ == '__main__':
     unittest.main()