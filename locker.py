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
