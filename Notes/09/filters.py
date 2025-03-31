import unittest

# Given a list of numbers, the function will make a new list with
# only the even values from the original list.
def are_even(list_of_nums):
   result_list = []
   index = 0
   while index < len(list_of_nums):
      if list_of_nums[index] % 2 == 0:
         result_list.append(list_of_nums[index])

      index += 1

   return result_list

# Let's look at a new way of using a for loop!
def are_even_for_loop(list_of_nums):
   result_list = []

   for value in list_of_nums: # New!  Exciting!
      if value % 2 == 0:
         result_list.append(value)

   return result_list

# Let's look at a shorthand way of the above!
def are_even_list_comprehension(list_of_nums):
   return [value for value in list_of_nums if value % 2 == 0]

# Tests!  We need tests!
class Tests(unittest.TestCase):
   def test_double1(self):
      init_list = [1, 2, 3, 4, 5, 6, 7, 8]
      doubled_list = are_even(init_list)

      self.assertEqual(doubled_list, [2, 4, 6, 8])
      self.assertEqual(init_list, [1, 2, 3, 4, 5, 6, 7, 8])

   def test_double2(self):
      init_list = [1, 2, 3, 4, 5, 6, 7, 8]
      doubled_list = are_even_for_loop(init_list)

      self.assertEqual(doubled_list, [2, 4, 6, 8])
      self.assertEqual(init_list, [1, 2, 3, 4, 5, 6, 7, 8])

   def test_double3(self):
      init_list = [1, 2, 3, 4, 5, 6, 7, 8]
      doubled_list = are_even_list_comprehension(init_list)

      self.assertEqual(doubled_list, [2, 4, 6, 8])
      self.assertEqual(init_list, [1, 2, 3, 4, 5, 6, 7, 8])

if __name__ == '__main__':
   unittest.main()
