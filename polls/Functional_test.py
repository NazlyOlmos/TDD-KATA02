from unittest import TestCase

from django.test import selenium

from selenium import webdriver

class FunctionalTest(TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000/')
        self.assertIn('Busco Ayuda', self.browser.title)