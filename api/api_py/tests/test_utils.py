from utils.utils import sum_users 

import unittest

class TestCase(unittest.TestCase):
  def testSumUsers(self):
    self.assertEqual(sum_users([1,2,3]), 3)
