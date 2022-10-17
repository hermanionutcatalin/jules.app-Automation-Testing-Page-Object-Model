import time
import unittest


from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager


from final_project.pagini.pagina_sign_up import PaginaSignUp


class TestPaginaSign(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://jules.app/sign-up")
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_quick_signup_sign_in_return(self):
        ps=PaginaSignUp(self.driver)
        ps.click_on_desired_element(PaginaSignUp.personal)
        ps.element_is_visible(PaginaSignUp.cont)
        ps.click_on_desired_element(PaginaSignUp.business)
        ps.click_on_desired_element(PaginaSignUp.sign_in_2)
        ps.s_check_url()
        time.sleep(5)
    #this method to be used with new fake email address updated in order to run
    def test_account_sign_up(self):
        ps = PaginaSignUp(self.driver)
        ps.click_on_desired_element(PaginaSignUp.personal)
        ps.click_on_desired_element(PaginaSignUp.cont)
        ps.input_data_into_field(PaginaSignUp.first_name,'John')
        ps.input_data_into_field(PaginaSignUp.first_name, Keys.ENTER)
        time.sleep(2)
        ps.input_data_into_field(PaginaSignUp.last_name,'Wick')
        ps.input_data_into_field(PaginaSignUp.last_name, Keys.ENTER)
        time.sleep(2)
        #replace fake email in the line below
        ps.input_data_into_field(PaginaSignUp.email,'banda1@securethering.com')
        ps.input_data_into_field(PaginaSignUp.email, Keys.ENTER)
        time.sleep(2)
        ps.input_data_into_field(PaginaSignUp.pass_s, 'Unique123!')
        ps.input_data_into_field(PaginaSignUp.pass_s, Keys.ENTER)
        time.sleep(2)
        ps.input_data_into_field(PaginaSignUp.pass_s_confirm,'Unique123!')
        ps.click_on_desired_element(PaginaSignUp.final_sign_up)
        time.sleep(2)
        self.driver.save_screenshot('sucessful.png')

