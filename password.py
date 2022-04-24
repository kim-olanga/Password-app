class User:
    """
    class that generates new instances of passwords
    """

    passwords_list = [] #List is empty..
    def __init__(self,first_name,last_name,email,passwords):
        # """
        # __init__ methods that helps us define properties for our objects.

        # Args:
        #     first_name:New password first name.
        #     last_name:New password last name.
        #     email:New password email address.
        #     password:New password password.
        # """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.passwords = passwords

    def save_passwords(self):
        """
        save_passwords method saves passwords objects into passwords_list
        """
        User.passwords_list.append(self)
    
    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        User.passwords_list = []

    def test_save_multiple_passwords(self):
        """
        test_save_multiple_passwords to check if we can save multiple passwords objects to our passwords_list
        """
        self.new_passwords.save_passwords()
        test_passwords = User("Cheryl","Hadassah","chadassah@gmail.com","Chada12")
        test_passwords.save_passwords()
        self.assertEqual(len(User.passwords_list),2)
    
    def delete_password(self):
        """
        delete_passwords method deletes a saved password from the passwords_list
        """
        User.passwords_list.remove(self)

    @classmethod
    def find_by_email(cls,email):
        """
        Method that takes in an email and returns a password that matches that email.
        Args:
            email: email to search for
        Returns:
            password of person that matches the email.
        """
        for passwords in cls.passwords_list:
            if passwords.email == email:
                return passwords


if __name__ =='__main__':
    unittest.main()    