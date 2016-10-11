from unittest import TestCase
from selenium import webdriver

class FunctionalTest(TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Nazly')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Olmos')

        experiencia = self.browser.find_element_by_id('id_aniosexperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollo Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('308366580')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('nolmos@gmail.com')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:/users/nazlyolmos/Downloads/imagen.jpg')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('nolmos')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element_by_id(By.XPATH,'//span[text()="Juan Pablo Arevalo')

        self.assertIn('Juan Daniel Arevalo', span.text)



