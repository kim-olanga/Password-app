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
        self.assertEqual(len(User.passwords_list),8)

 def test_save_multiple_passwords(self):
        """
        test_save_multiple_passwords to check if we can save multiple passwords obejects to our passwords_list
        """
        self.new_passwords.save_passwords()
        test_passwords = User("Cheryl","Hadassah","chadassah@gmail.com","Chada12")
        test_passwords.save_passwords()
        self.assertEqual(len(User.passwords_list),7)

 def test_delete_passwords(self):
        """
        test_delete_passwords to test if we can remove a password from our password list
        """
        self.new_passwords.save_passwords()
        test_passwords = User("Cheryl","Hadassah","chadassah@gmail.com","Chada12")
        test_passwords.save_passwords()
        self.new_passwords.delete_password()
        self.assertEqual(len(User.passwords_list),1)

 def test_find_password_by_email(self):
       """
       test to check if we can find a password by email and display information
       """
       self.new_passwords.save_passwords()
       test_passwords = User("Cheryl","Hadassah","chadassah@gmail.com","Chada12")
       test_passwords.save_passwords()
       found_passwords = User.find_by_email("chadassah@gmail.com")
       self.assertEqual(found_passwords.first_name,test_passwords.first_name)

 def test_passwords_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the passwords.
        """
        self.new_passwords.save_passwords()
        test_passwords =User("Cheryl","Hadassah","chadassah@gmail.com","Chada12")
        test_passwords.save_passwords()
        passwords_exists = User.passwords_exists("chadassah@gmail.com")
        self.assertTrue(passwords_exists)

if __name__ == '__main__':
    unittest.main()