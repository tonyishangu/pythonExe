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

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credentials('Gmail','Tony_ishangu','yx5Gij43')

    def test_init(self):
        self.assertEqual(self.new_credential.account,'Gmail')
        self.assertEqual(self.new_credential.username,'Tony_ishangu')
        self.assertEqual(self.new_credential.password,'yx5Gij43')
            
    def save_credential_test(self):
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        Credentials.credentials_list = []

    def test_save_many_accounts(self):
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","tonnieishangu","Mfh45hfk") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","tonnieishangu","Mfh45hfk")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentialr(self):

        self.new_credential.save_details()
        test_credential = Credentials("Twitter","tonnieishangu","Mfh45hfk") 
        test_credential.save_details()

        the_credential = Credentials.find_credential("Twitter")

        self.assertEqual(the_credential.account,test_credential.account)

    def test_credential_exist(self):
        self.new_credential.save_details()
        the_credential = Credentials("Twitter", "tonnieishangu", "Mfh45hfk")  
        the_credential.save_details()
        credential_is_found = Credentials.if_credential_exist("Twitter")
        self.assertTrue(credential_is_found)

    def test_display_all_saved_credentials(self):   
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)


if __name__ == "__main__":
    unittest.main()