import unittest

class NoExperienceError(Exception):
    pass

class Employee:
    def __init__(self):
        pass
        
    def hire(self):
        raise NoExperienceError

class Test(unittest.TestCase):
    def setUp(self):
        self.odd_value = 5
        self.even_value = 6
        self.string = "XYZ"
        
    def test_is_odd(self):
        self.assertTrue(self.odd_value % 2 != 0)
        
    def test_is_xyz(self):
        self.assertEqual(self.string.lower(), "xyz")
        
    def test_value_not_none(self):
        value = True
        self.assertIsNotNone(value)
    
    def test_in(self):
        self.assertIn('xyz', [1, 3.13, "xyz"])
        
    def test_not_in(self):
        self.assertNotIn('xyz', [1, 3.13, "xy"])
        
    def test_no_experience_error_raised(self):
        self.employee = Employee()
        
        with self.assertRaises(NoExperienceError):
            self.employee.hire()
            
    def test_is_not_numeric(self):
        value = "abc"
        self.assertNotIsInstance(value, int) 
        
        
    
    
if __name__ == "__main__":
    unittest.main()