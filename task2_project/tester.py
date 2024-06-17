import unittest
from app import Solution
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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

    # New tests
    def test_large_range(self):
        self.assertEqual(self.solution.longestConsecutive(list(range(1, 10001))), 10000)

    def test_unsorted_list(self):
        self.assertEqual(self.solution.longestConsecutive([10, 5, 12, 3, 55, 7, 6, 8, 4, 11]), 6)

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_homepage_title(self):
        self.driver.get('http://127.0.0.1:5000')
        self.assertIn("Longest Consecutive Sequence", self.driver.title)

    def test_form_submission(self):
        self.driver.get('http://127.0.0.1:5000')
        input_box = self.driver.find_element(By.ID, 'nums')
        input_box.send_keys('100, 4, 200, 1, 3, 2')
        input_box.send_keys(Keys.RETURN)
        time.sleep(1)  # Wait for the page to load
        result = self.driver.find_element(By.TAG_NAME, 'h2').text
        self.assertIn('Result: 4', result)

    def test_invalid_input(self):
        self.driver.get('http://127.0.0.1:5000')
        input_box = self.driver.find_element(By.ID, 'nums')
        input_box.send_keys('a, b, c')
        input_box.send_keys(Keys.RETURN)
        time.sleep(1)  # Wait for the page to load
        result = self.driver.find_element(By.TAG_NAME, 'h2').text
        self.assertIn('Invalid input', result)

if __name__ == '__main__':
    unittest.main()
