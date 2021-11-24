from coding_challenge import challenge
import sys
import unittest
import os

path_parent = os.path.dirname(os.getcwd())
sys.path.insert(1,path_parent)

class unit_cod_cha(unittest.TestCase,challenge):
     def test_url(self):
         self.assertAlmostEqual(self.unit_test("https://reqres.in/api/users?page=2"),200)


obj = unit_cod_cha()
obj.test_url()
