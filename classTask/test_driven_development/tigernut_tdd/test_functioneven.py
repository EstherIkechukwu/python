import unittest
import functioneven
import functionvowel
import functionanagram
import functionprime
import functionpalindrome
import functionaverage
import functionreversed
import functionodd
import functionsumofdigits
import functionacronym
import functionmagicnumbers
import functiongetnumbermerged

class TestSumEvenFunction(unittest.TestCase):
	def test_that_get_even_numbers_exist(self):
		x = [1,2,3,4,5]
		functioneven.get_even_numbers(x)

	def test_that_get_even_numbers_returns_correct_value(self):
		actual = functioneven.get_even_numbers([1,2,3,4,6,9])
		expected = 12
		self.assertEqual(actual, expected)
		actual = functioneven.get_even_numbers([4,3,4,8,9])
		expected = 16
		self.assertEqual(actual, expected)

	def test_that_get_vowel_exist(self):
		char = "python is sweet"
		actual = functionvowel.get_vowel(char)
		expected = 4
		self.assertEqual(actual, expected)

	def test_that_get_vowel_returns_correct_value(self):
		char1 = "python is bitter"
		actual = functionvowel.get_vowel(char1)
		expected = 4
		self.assertEqual(actual, expected)

	def test_that_get_Anagram_exist(self):
		word1 = "silent"
		word2 = "listen"
		actual = functionanagram.get_Anagram(word1, word2)
		expected = True
		self.assertEqual(actual, expected)

	def test_that_get_Anagram_returns_correct_value(self):
		word1 = "evil"
		word2 = "live"
		actual = functionanagram.get_Anagram(word1, word2)
		expected = True
		self.assertEqual(actual, expected)

	def test_that_get_prime_number_exist(self):
		actual = functionprime.get_prime_number(7)
		expected = True
		self.assertEqual(actual, expected)

	def test_that_get_get_palindrome_exist(self):
		actual = functionpalindrome.get_palindrome("madam")
		expected = True

	def test_that_get_palindrome_correct_value(self):
		actual = functionpalindrome.get_palindrome("bacab")
		expected = True
	
	def test_that_get_average_exist(self):
		x = [12, 35 ,9, 4, 8]
		actual = functionaverage.get_average(x)
		expected = 13.6

	def test_that_get_average_correct_value(self):
		actual = functionaverage.get_average([1,2,3,4,6])
		expected = 3.2

	def test_that_get_string_reversed_exist(self):
		actual = functionreversed.get_string_reversed("hello")
		expected = "olleh"

	def test_that_get_string_reversed_correct_value(self):
		actual = functionreversed.get_string_reversed("esther")
		expected = "rehtse"

	def test_that_get_sum_of_odd_digits_exist(self):
		x = [1,2,3,4,5]
		functionodd.get_sum_of_odd_digits(x)

	def test_that_get_sum_of_odd_digits_returns_correct_value(self):
		actual = functionodd.get_sum_of_odd_digits([1,5,8,9,4])
		expected = 15
		self.assertEqual(actual, expected)

	def test_that_get_sum_of_digits_exist(self):
		x = [2, 6, 9, 12, 14, 18]
		functionsumofdigits.get_sum_of_digits(x)

	def test_that_get_sum_of_digits_returns_correct_value(self):
		actual = functionsumofdigits.get_sum_of_digits([1,5,8,9,4])
		expected = 27
		self.assertEqual(actual, expected)

	def test_that_get_acronym_exist(self):
		functionacronym.get_acronym("Portable Network Graphics")

	def test_that_get_magic_numbers_exist(self):
		x = [1,2,3,4]
		functionmagicnumbers.get_magic_numbers(x)

	def test_that_get_magic_numbers_returns_correct_value(self):
		actual = functionmagicnumbers.get_magic_numbers([1,2,3,4,5,6])
		expected = 105
		self.assertEqual(actual, expected)

	def test_that_get_number_merged_exist(self):
		numberOne = [3,4,9,10]
		numberTwo = [1,5,7,8]
		functiongetnumbermerged.get_number_merged(numberOne, numberTwo)

	def test_that_get_number_merged_returns_correct_value(self):
		numberOne = [3,4,9,10,-5]
		numberTwo = [1,5,7,8,32]
		actual = functiongetnumbermerged.get_number_merged(numberOne, numberTwo)
		expected = [-5,1,3,4,5,7,8,9,10,32]
		self.assertEqual(actual, expected)

		













	

	

	
