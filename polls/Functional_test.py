from unittest import TestCase
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_ver_detalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Nazly Olmos"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Nazly Olmos"]')

        self.assertIn('Nazly Olmos', h2.text)

    def test_registro(self):
        self.browser.get('http://localhost:8000')

        link = self.browser.find_element_by_id('id_register')
        link.click()

        time.sleep(5)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Nazly')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Olmos')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollo Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('308366580')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('nolmos@gmail.com')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:\\Users\\diego\\Pictures\\diego.jpg')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('yego235')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()

        self.browser.implicitly_wait(5)
        span = self.browser.find_element(By.XPATH, '//span[text()="Nazly Olmos"]')

        self.assertIn('Nazly Olmos', span.text)

    def test_login(self):
        self.browser.get('http://localhost:8000')

        link = self.browser.find_element_by_id('id_login')
        link.click()

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('yego23')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonLogin = self.browser.find_element_by_id('id_login')
        botonLogin.click()

        p = self.browser.find_element(By.XPATH, "//p[text()='Nazly Olmos']")

    def test_comment(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Nazly Olmos"]')
        span.click()

        correo = self.browser.find_element_by_id('correo')
        correo.send_keys('diegofruizs@gmail.com')

        comentario = self.browser.find_element_by_id('comentario')
        comentario.send_keys('Hola saludos')

        btnAgregar = self.browser.find_element_by_id('btnComentar')
        btnAgregar.click()

    def test_edit(self):
        self.browser.get('http://localhost:8000')

        link = self.browser.find_element_by_id('id_login')
        link.click()

        self.browser.implicitly_wait(9)

        username = self.browser.find_element_by_id('id_username')
        username.send_keys('yego23')

        password = self.browser.find_element_by_id('id_password')
        password.send_keys('clave123')

        botonLogin = self.browser.find_element_by_id('id_login')
        botonLogin.click()

        time.sleep(5)

        link = self.browser.find_element_by_id('id_editar')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.clear()
        nombre.send_keys('Josesito')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        nombre.clear()
        apellidos.send_keys('Obama')

        id_aniosExperiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        nombre.clear()
        id_aniosExperiencia.send_keys(4)

        grabarBtn = self.browser.find_element_by_id('id_grabar')

        grabarBtn.click()

        logoutBtn = self.browser.find_element_by_id('id_logout')
        logoutBtn.click()

        time.sleep(15)

        span = self.browser.find_element(By.XPATH, "//span[text()='Josesito Obama']")

        self.assertIn('Josesito Obama', span.text)
