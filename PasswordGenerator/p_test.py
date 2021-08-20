import unittest
from passlock import User, Credentials

class TestClass(unittest.TestCase):

    def setUp(self):
        self.new_user = User('Tonyishangu', 'XyZ3thf1')

    def test_init(self):
        self.assertEqual(self.new_user.username,'Tonyishangu')
        self.assertEqual(self.new_user.password,'XyZ3thf1')

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


if __name__ == "__main__":
    unittest.main()