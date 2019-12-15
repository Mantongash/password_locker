############### BDD #######################
# 1. Create Password Locker Account.
# 2. Store account credentials.
# 3. Create new password credentials.
# 4. Input my own password.
# 5. View saved account credentials.
# 5. Delete an account credential.
##########################################
import unittest
from locker import Users


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

    #Save multiple users
    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple users
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = Users("test", "test")  # new user
        test_user.save_user()
        self.assertEqual(len(Users.user_list), 2)





if __name__ == "__main__":
    unittest.main()
