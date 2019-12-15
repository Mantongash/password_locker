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

    def setup(self):
