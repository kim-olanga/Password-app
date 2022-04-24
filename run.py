#!/usr/bin/env python3.8
from passwords import User

def create_passwords(fname,lname,email,passwords):
    '''
    Function to create a new passwords
    '''
    new_passwords = User(fname,lname,email,passwords)
    return new_passwords

def save_passwords(passwords):
    '''
    Function to save passwords
    '''
    password.save_passwords()

def delete_passwords(passwords):
    '''
    Function to delete a passwords
    '''
    passwords.delete_passwords()

def find_passwords(email):
    '''
    Function that finds passwords by email and returns the passwords
    '''
    return User.find_by_email(email)

def check_existing_passwords(email):
    '''
    Function that check if passwords exists with that email and return a Boolean
    '''
    return User.passwords_exist(email)

def display_passwords():
    '''
    Function that returns all the saved passwords
    '''
    return User.display_passwords()