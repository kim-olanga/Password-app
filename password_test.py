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

 def test_save_passwords(self):
        """
        test_save_passwords test case to test if the contact object is saved into the passwords_list
        """
        self.new_passwords.save_passwords()
        self.assertEqual(len(User.passwords_list),3)

 def test_save_multiple_passwords(self):
        """
        test_save_multiple_passwords to check if we can save multiple passwords obejects to our passwords_list
        """
        self.new_passwords.save_passwords()
        test_passwords = User("Cheryl","Hadassah","chadassah@gmail.com","Chada12")
        test_passwords.save_passwords()
        self.assertEqual(len(User.passwords_list),2)

 def test_delete_passwords(self):
        """
        test_delete_passwords to test if we can remove a password from our password list
        """
        self.new_passwords.save_passwords()
        test_passwords = User("Cheryl","Hadassah","chadassah@gmail.com","Chada12")
        test_passwords.save_passwords()
        self.new_passwords.delete_password()
        self.assertEqual(len(User.passwords_list),1)

if __name__ == '__main__':
    unittest.main()