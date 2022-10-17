import unittest
import time


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from final_project.pagini.pagina_home import PaginaHome


class TestPaginaHome(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://jules.app/sign-in")
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_invalid_mail_and_blank_pass(self):
        ph=PaginaHome(self.driver)
        ph.input_data_into_field(PaginaHome.mail_field,'herman')
        ph.show_invalid_message(PaginaHome.mail_mess)
        ph.input_data_into_field(PaginaHome.pass_field,'a')
        ph.delete_field_data(PaginaHome.pass_field)
        ph.show_invalid_message(PaginaHome.pass_mess)
        time.sleep(5)

    def test_if_login_button_enables_on_valid_mail(self):
        ph = PaginaHome(self.driver)
        ph.input_data_into_field(PaginaHome.mail_field, 'hermanionutcatalin@yahoo.ro')
        ph.input_data_into_field(PaginaHome.pass_field, 'X123')
        ph.element_is_visible(PaginaHome.login_btn)
        time.sleep(5)

    def test_if_invalid_login_message_shown(self):
        ph = PaginaHome(self.driver)
        ph.input_data_into_field(PaginaHome.mail_field, 'hermanionutcatalin@yahoo.ro')
        ph.input_data_into_field(PaginaHome.pass_field, 'X123')
        ph.click_on_desired_element(PaginaHome.login_btn)
        ph.show_invalid_message(PaginaHome.invalid_mess)
        time.sleep(5)

    def test_forgot_pass_section_and_back_to_login(self):
        ph = PaginaHome(self.driver)
        ph.click_on_desired_element(PaginaHome.pass_forgot)
        ph.input_data_into_field(PaginaHome.forgot_mail, 'hermanionutcatalin@yahoo.ro')
        ph.element_is_visible(PaginaHome.send_email)
        self.driver.back()
        time.sleep(5)

