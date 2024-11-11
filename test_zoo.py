import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(6), 50)  # Class1: 0-12
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
        self.assertEqual(self.zoo.get_ticket_price(10), 50)

    def test_teenager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(16), 100)  # Class2: 13-20
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(26), 150)  # Class3: 21-60
        self.assertEqual(self.zoo.get_ticket_price(21), 150)  
        self.assertEqual(self.zoo.get_ticket_price(60), 150)  



    def test_senior_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(66), 100)  # Class4: >60
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

    def test_invalid_age_negative(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 'error')  # Class4: >60  # Class5: invalid value < 0




if __name__ == '__main__':
    unittest.main()