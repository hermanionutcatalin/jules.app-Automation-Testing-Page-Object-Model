from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from final_project.pagini.pagina_baza import PaginaBaza
from final_project.pagini.pagina_home import PaginaHome


class PaginaSignUp(PaginaHome):

    personal = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/label/span[1]/span/input')
    business = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[1]/label/span[1]/span/input')
    cont = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[5]/button/span[1]')
    sign_in_2 = (By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[4]/a/button/span[1]')
    first_name = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    last_name = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    email = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    pass_s=(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    pass_s_confirm=(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    final_sign_up=(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/button')



    def s_check_url(self):
        url = self.driver.current_url
        print("The current url is:" + str(url))
