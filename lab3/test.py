import unittest
from server import f

tc = unittest.TestCase('__init__')

tc.assertEqual(f(2), '4')
tc.assertEqual(f(3), '6')
tc.assertEqual(f(4), '8')
tc.assertEqual(f(5), '10')
