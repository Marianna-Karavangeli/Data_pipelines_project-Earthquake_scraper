import unittest
import pandas as pd

from Earthquake_scraper.rds_uploader import rds_uploader


class RdsUploaderTestCase(unittest.TestCase):
    def test_rds_uploader(self):

        actual_value = 'Your dataset was uploaded successfully!'
        expected_value = rds_uploader()

        self.assertEqual(actual_value, expected_value)  # <6>
