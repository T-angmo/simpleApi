# import unittest

# # from flask import app
# # from app import plus
# # from app import is_prime
# from app import app

# # class TestAPI(unittest.TestCase):
# #     def test_plus(self):
# #         self.assertEqual(plus(5, 6), '11')


# class TestAPI(unittest.TestCase):
#     def setUp(self):
#         # Set up a test client
#         self.app = app.test_client()
#         self.app.testing = True
#     def true_when_x_17(self):
#         response = self.app.get('/is_prime/17')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.get_json()['result'], True)
#     def false_when_x_36(self):
#         response = self.app.get('/is_prime/36')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.get_json()['result'], False)
#     def true_when_x_13219(self):
#         response = self.app.get('/is_prime/13219')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.get_json()['result'], False)

# if __name__ == '__main__':
#     unittest.main()





# import unittest
# from flask import app
# from app import app

# class AppTestCase(unittest.TestCase):
#     def setUp(self):
#         self.app = app.test_client()
#         self.app.testing = True
#     def true_when_x_is_17(self):
#         response = self.client.get("/is_prime/17")
#         self.assertEqual(response.status_code)
#         self.assertTrue(response.json())
#     def true_when_x_is_36(self):
#         response = self.client.get("/is_prime/36")
#         self.assertEqual(response.status_code)
#         self.assertFalse(response.json())
#     def true_when_x_is_13219(self):
#         response = self.client.get("/is_prime/13219")
#         self.assertEqual(response.status_code)
#         self.assertTrue(response.json())
        
# if __name__ == "__main__":
#     unittest.main()




# import unittest
# from app import  mul5

# class TestAPI(unittest.TestCase):

#     def test_x_is_1(self):
#         self.assertEqual(mul5(1), '5.0')
#     def test_x_is_neg10(self):
#         self.assertEqual(mul5(-10), '-50.0')
#     def test_x_is_1dot5(self):
#         self.assertEqual(mul5(1.5), '7.5')


# if __name__ == '__main__':
#     unittest.main()

    # test_case = AppTestCase()

    # # Manually calling setup and test methods
    # test_case.setUp()
    # test_case.is_prime_true()
    # test_case.is_prime_false()
    # test_case.is_prime_edge_case()


import unittest
from app import  power

class TestAPI(unittest.TestCase):

    def test_x_is_5_3(self):
        self.assertEqual(power(5, 3), '125.0')

    def test_x_is_4_0(self):
        self.assertEqual(power(4, 0), '1.0')

    def test_x_is_9_half(self):
        self.assertEqual(power(9, 0.5), '3.0')


if __name__ == '__main__':
    unittest.main()

