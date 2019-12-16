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

    @classmethod
    def user_exists(cls, name):
        '''
        Method that checks if a user exists from the user list.
        Args:
            name: Username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.username == name:
                return True

        return False


class Credentials:
    """
    This class stores user credentials
    """
    credentials_list = []

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
        Credentials.credentials_list.append(self)

        # Delete credential function
    def delete_credentials(self):
        """
        Function for saving credentials
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the contact list
        '''
        return cls.credentials_list

    @classmethod
    def credentials_exists(cls, online_account):
        '''
        Method that checks if a credential exists from the credentials list.
        Args:
            account_name: account_name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for account in cls.credentials_list:
            if account.account_username == online_account:
                return True

        return False
