#!/usr/bin/env python3.6
from locker import Users, Credentials
from pynput.keyboard import Key, Controller
from termcolor import colored
import time
# import pyperclip

# Users


def create_user(uname, password):
    '''
    Function to create a new user
    '''
    new_user = Users(uname, password)
    return new_user


def save_user(user):
    '''
    Function to save a user
    '''
    user.save_user()


def del_cont(user):
    '''
    Function to delete a user
    '''
    user.delete_contact()

    # Credentials


def create_credential(uname, account, account_username, account_password):
    '''
    Function to create a new credential
    '''
    new_user = Credentials(uname, account, account_username, account_password)
    return new_user


def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()


def del_cred(credentials):
    '''
    Function to delete a contact
    '''
    credentials.delete_credentials()


def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_credentials()


def main():
    # keyboard = Controller()
    # time.sleep(2)
    print("Hello, WELCOME to THE PASSWORD LOCKER. What is your name, please :) ?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do today?")
    print('\n')

    while True:
        print("Use these short codes : ca - create a new account,  li - log in, dc - display credentials, cc - create credential - ex - exit the password locker")

        short_code = input().lower()

        if short_code == 'ca':
            print(
                "Awesome choice: Kindly provide me with a username and a password")
            print('\n')
            print("*"*100)
            print('\n')

            print("Username:")
            uname = input()

            print("Password:")
            password = input()

           # create and save new user.
            save_user(create_user(
                uname, password))
            print('\n')
            print(
                f"Account Details: Username ** {uname} ** \nPassword ** {password} **")
            print('\n')

        elif short_code == "li":
            print("Kindly enter your details to log-in")
            print("Username:")
            username = input()

            print("Password:")
            password = input()
            for user in Users.user_list:
                if user == username:
                    print("User is already registered")
                else:
                    print("You are logged in")
        # elif short_code ==

        # elif short_code == 'dc':

            #     if display_contacts():
            #         print("Here is a list of all your contacts")
            #         print('\n')

            #         for contact in display_contacts():
            #             print(
            #                 f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

            #         print('\n')
            #     else:
            #         print('\n')
            #         print("You dont seem to have any contacts saved yet")
            #         print('\n')

            # elif short_code == 'fc':

            #     print("Enter the number you want to search for")

            #     search_number = input()
            #     if check_existing_contacts(search_number):
            #         search_contact = find_contact(search_number)
            #         print(
            #             f"{search_contact.first_name} {search_contact.last_name}")
            #         print('-' * 20)

            #         print(
            #             f"Phone number.......{search_contact.phone_number}")
            #         print(f"Email address.......{search_contact.email}")
            #     else:
            #         print("That contact does not exist")

            # elif short_code == "ex":
            #     print("Bye .......")
            #     break
            # else:
            #     print("I realsly didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()
