import unittest
from password import User
import pyperclip

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

 def test_display_all_passwords(self):
        '''
        method that returns a list of all passwords saved
        '''

        self.assertEqual(User.display_passwords(),User.passwords_list)

 def main():
    print("Hello Welcome to your contact list. What is your name?")
            user_name = input()

            print(f"Hello {user_name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
                            print ('\n')
                            print(f"New Contact {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_contacts():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for contact in display_contacts():
                                            print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_contacts(search_number):
                                    search_contact = find_contact(search_number)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_contact.phone_number}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
    unittest.main()