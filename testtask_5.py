import unittest
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest_sequence = 0

        for num in num_set:
            # Only check for the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_sequence = 1

                # Check the length of the sequence starting from current_num
                while current_num + 1 in num_set:
                    current_num += 1
                    current_sequence += 1

                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence

class TestLongestConsecutiveSequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.longestConsecutive([]), 0)

    def test_single_element(self):
        self.assertEqual(self.solution.longestConsecutive([1]), 1)

    def test_no_consecutive(self):
        self.assertEqual(self.solution.longestConsecutive([10, 5, 100]), 1)

    def test_consecutive(self):
        self.assertEqual(self.solution.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_mixed_elements(self):
        self.assertEqual(self.solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)

    def test_duplicates(self):
        self.assertEqual(self.solution.longestConsecutive([1, 2, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(self.solution.longestConsecutive([-1, -2, -3, -4, 0, 1, 2, 3, 4]), 9)

    def test_all_elements_same(self):
        self.assertEqual(self.solution.longestConsecutive([5, 5, 5, 5, 5]), 1)

    def test_large_range(self):
        self.assertEqual(self.solution.longestConsecutive([-50, -49, 50, 51, 52, 53, 54, 55, -48, -47, 0, 1, 2, 3]), 9)

    def test_gaps_in_sequence(self):
        self.assertEqual(self.solution.longestConsecutive([10, 1, 3, 5, 2, 4, 6, 100, 101, 102, 103, 104]), 6)

    def test_large_input(self):
        self.assertEqual(self.solution.longestConsecutive(list(range(1000000))), 1000000)

if __name__ == '__main__':
    unittest.main()
