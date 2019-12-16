class Users:
    """
    A class to store user log in details.
    """
    user_list = []  # Blank user list to store user details

    def __init__(self, username, password):
        """
        Defining the init method (constructor) that will be used to create new user instances
        """
        self.username = username
        self.password = password

    # Save user function
    def save_user(self):
        """
        Function for saving users
        """
        Users.user_list.append(self)

    # Delete user function
    def delete_user(self):
        """
        Function to delete a user from the user list
        """
        Users.user_list.remove(self)


class Credentials:
    """
    This class stores user credentials
    """

    def __init__(self, username, account, account_username, account_password):
        """
        Init method for creating new instances of account credentials
        """
        self.username = username
        self.account = account
        self.account_username = account_username
        self.account_password = account_password

            # Save credential function
    def save_credentials(self):
        """
        Function for saving credentials
        """
        Users.user_list.append(self)
