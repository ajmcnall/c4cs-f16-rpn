import unittest

import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_subtract(self):
		result = rpn.calculate("5 3 -")
		self.assertEqual(2, result)

	def test_multiply(self):
		result = rpn.calculate("4 4 *")
		self.assertEqual(16, result)
	def test_divide(self):
		result = rpn.calculate("15 3 /")
		self.assertEqual(5, result)
	def test_carat(self):
		result = rpn.calculate("7 2 ^")
		self.assertEqual(49, result)

	def test_toomanythings(self):
		with self.assertRaises(TypeError):
			rpn.calculate('1 2 3 +')
