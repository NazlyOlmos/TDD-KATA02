from unittest import TestCase
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_edit(self):
        self.browser.get('http://localhost:8000')

        link = self.browser.find_element_by_id('id_login')
        link.click()

        self.browser.implicitly_wait(5)

        username = self.browser.find_element_by_id('username')
        username.send_keys("yego23")

        password = self.browser.find_element_by_id('password')
        password.send_keys("clave123")

        login_button = self.browser.find_element_by_id('id_login_button')
        login_button.click()

        time.sleep(5)

        link = self.browser.find_element_by_id('id_editar')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        self.browser.execute_script("arguments[0].value = ''", nombre)
        nombre.send_keys('Josesito')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        self.browser.execute_script("arguments[0].value = ''", apellidos)
        apellidos.send_keys('Obama')

        id_aniosExperiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        self.browser.execute_script("arguments[0].value = ''", id_aniosExperiencia)
        id_aniosExperiencia.send_keys(4)

        correo = self.browser.find_element_by_id('id_correo')
        self.browser.execute_script("arguments[0].value = ''", correo)
        correo.send_keys('alguien@gmail.com')

        grabarBtn = self.browser.find_element_by_id('id_grabar')

        grabarBtn.click()

        logoutBtn = self.browser.find_element_by_id('id_logout')
        logoutBtn.click()

        time.sleep(15)

        span = self.browser.find_element(By.XPATH, "//span[text()='Josesito Obama']")

        self.assertIn('Josesito Obama', span.text)
