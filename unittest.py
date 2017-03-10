import unittest
from solution_prime import prime_number

class TestAnalysis(unittest.TestCase):

   def test_for_right_primenumber(self):
       value = analysis()
       self.assertEqual( value , 1)
   def test_for_ten_in_results(self):
       value = analysis()
       self.assertEqual(value , 10)
   def test_for_range_of_ten_numbers(self):
       data = [2,3, 5, 7]
       value = analysis()
       self.assertEqual(value , data)
   def test_for_all_of_primeno(self):
       testlist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
       value = analysis()
self.assertListEqual(value , testlist)