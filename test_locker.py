############### BDD #######################
# 1. Create Password Locker Account.
# 2. Store account credentials.
# 3. Create new password credentials.
# 4. Input my own password.
# 5. View saved account credentials.
# 5. Delete an account credential.
##########################################
import unittest
from locker import Users, Credentials


class TestUsers(unittest.TestCase):
    """
    A class that inherits the TestCase class from the unittest module.
    This is a very important step.
    """

    def setUp(self):
        """
        This runs before the test cases are run
        """
        self.new_user = Users("mantongash", "anthony")  # A new user

    def test_init(self):
        """
        This is to make sure that the user is initialized properly
        """
        self.assertEqual(self.new_user.username, "mantongash")
        self.assertEqual(self.new_user.password, "anthony")

    # Test for saving contacts
    def test_save_users(self):
        """
        Test to check the save feature
        """

        self.new_user.save_user()  # saving the new cont# setup and class creation up here

    # Tear down function
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Users.user_list = []

    # Save multiple users
    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple users
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = Users("test", "test")  # new user
        test_user.save_user()
        self.assertEqual(len(Users.user_list), 2)

    # Test to delete User Accounts
    def test_delete_users(self):
        '''
        test_delete_users to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = Users("test", "test")  # new user
        test_user.save_user()
        self.new_user.delete_user()  # Deleting a user object
        self.assertEqual(len(Users.user_list), 1)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = Users("test", "test")  # new user
        test_user.save_user()

        user_exists = Users.user_exist("test")

        self.assertTrue(user_exists)


class TestCredentials(unittest.TestCase):
    """
    Class to test the account credentials
    """

    def setUp(self):
        """
        This runs before the tests
        """
        self.new_credentials = Credentials(
            "mantongash", "Facebook", "mantongash", "mantongash")

    def test_credentials_init(self):
        """
        Test case to show that credentials are well initialized.
        """
        self.assertEqual(self.new_credentials.username, "mantongash")
        self.assertEqual(self.new_credentials.account, "Facebook")
        self.assertEqual(self.new_credentials.account_username, "mantongash")
        self.assertEqual(self.new_credentials.account_password, "mantongash")

       # Test for saving credentials
    def test_save_credentials(self):
        """
        Test to check the save feature
        """

        self.new_credentials.save_credentials()  # saving the new credentials

    # Tear down function
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    # Save multiple users
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_users to check if we can save multiple users
        objects to our user_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "test", "Facebook", "test", "test")  # new credentials
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    # Test to delete Credentials
    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a user from our user list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "test", "Facebook", "test", "test")  # new user
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()  # Deleting a user object
        self.assertEqual(len(Credentials.credentials_list), 1)


if __name__ == "__main__":
    unittest.main()
