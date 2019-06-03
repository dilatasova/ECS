"""Tech assessment"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Frontend(unittest.TestCase):
    """
    Tech test
    """

    def setUp(self):
        self.driver = webdriver.Chrome()

    def wait_for_element_exists(self, css_selector, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

    @staticmethod
    def calculate_center(arr):
        """
        Takes an array of numbers and returns the first index at which the sum of the numbers on the left is equal to the numbers on the right.
        Returns None if no suitable index found.
        """
        for i in range(1, len(arr)):
            if sum(arr[:i]) == sum(arr[i+1:]):
                return i
        else:
            return None

    def test_ECS_submission(self):
        """
        Perform task on test page.
        """

        # go to page, click render button and wait for challenge section to exist.
        self.driver.get('http://localhost:3000/')
        self.driver.find_element_by_css_selector(
            '[data-test-id="render-challenge"]').click()
        self.wait_for_element_exists("#challenge")

        # get the arrays fromthe page, then calculate centers
        rows = self.driver.find_elements_by_css_selector('#challenge table tr')
        arrays = [list(map(int, row.text.split())) for row in rows]
        centers = list(map(self.calculate_center, arrays))
        centers.append("Gabriel Carpenter")  # add name for submission

        # fill out the submission form and submit
        for i, c in enumerate(centers, 1):
            self.driver.find_element_by_css_selector(
                f'[data-test-id="submit-{i}"]').send_keys(str(c))
        self.driver.find_element_by_css_selector('#challenge button').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(exit=False)
