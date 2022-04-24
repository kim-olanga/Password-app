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

    def