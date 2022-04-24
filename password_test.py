import unittest
from password import User

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the User class behaviors.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        set up method to run before each test cases.
        """
        self.new_passwords = User("Kimzy","Eve","kimzyeve@gmail.com","Ayubu12")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_passwords.first_name,"Kimzy")
        self.assertEqual(self.new_passwords.last_name,"Eve")
        self.assertEqual(self.new_passwords.email,"kimzyeve@gmail.com")
        self.assertEqual(self.new_passwords.passwords,"Ayubu12")

if __name__ == '__main__':
    unittest.main()