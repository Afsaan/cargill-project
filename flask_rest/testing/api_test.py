import unittest
import requests

class TestAPI(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000'
    role_endpoint = 'role/'
    team_endpoint = 'team/'
    associate_role_endpoint = 'team/ML/'
    manage_role_endpoint = 'map-role/'

    def test_1_get_roles(self):

        response = requests.get(f"{self.base_url}/{self.role_endpoint}")
        self.assertEqual(response.status_code, 200)
        print('[INFO] test case 1 passed')
        # self.assertDictEqual(response.json()[0], response_body)

    def test_2_post_role(self):
        test_data = {
            "role":"tester"
        }

        response = requests.get(f"{self.base_url}/{self.role_endpoint}", json = test_data )
        self.assertEqual(response.status_code, 200)
        print('[INFO] test case 2 passed')

    def test_3_get_team(self):

        response = requests.get(f"{self.base_url}/{self.team_endpoint}")
        self.assertEqual(response.status_code, 200)
        print('[INFO] test case 3 passed')
        # self.assertDictEqual(response.json()[0], response_body)

    def test_4_post_role(self):
        test_data = {
            "team":"tester"
        }

        response = requests.get(f"{self.base_url}/{self.team_endpoint}", json = test_data )
        self.assertEqual(response.status_code, 200)
        print('[INFO] test case 4 passed')

    def test_5_get_associated_role(self):

        response = requests.get(f"{self.base_url}/{self.associate_role_endpoint}")
        self.assertEqual(response.status_code, 200)
        print('[INFO] test case 5 passed')
        # self.assertDictEqual(response.json()[0], response_body)

    def test_6_map_role(self):
        test_data = {
            "team":"tester_team",
            "role":"tester_role"
        }

        response = requests.get(f"{self.base_url}/{self.manage_role_endpoint}", json = test_data )
        self.assertEqual(response.status_code, 200)
        print('[INFO] test case 6 passed')

    
if __name__ == '__main__':
    tester = TestAPI()
    tester.test_1_get_roles()
    tester.test_2_post_role()
    tester.test_3_get_team()
    tester.test_4_post_role()
    print('[INFO] all the test case passed')


