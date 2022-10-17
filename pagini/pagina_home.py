from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from final_project.pagini.pagina_baza import PaginaBaza


class PaginaHome(PaginaBaza):

    mail_field=(By.CSS_SELECTOR, '#root > div > div.css-1kq6ix3 > form > div > div:nth-child(1) > div > div > input')
    pass_field=(By.XPATH,'//*[@id="root"]/div/div[2]/form/div/div[2]/div/div/input')
    login_btn=(By.XPATH,'//*[@id="root"]/div/div[2]/form/div/div[3]/button')
    pass_forgot=(By.XPATH,'//*[@id="root"]/div/div[2]/form/div/div[3]/a')
    app_store=(By.XPATH,'//*[@id="root"]/div/div[3]/div/div[2]/div[1]/a/img')
    gog_play=(By.XPATH,'//*[@id="root"]/div/div[3]/div/div[2]/div[2]/a/img')
    faq=(By.XPATH,'//*[@id="root"]/div/div[3]/div/div[3]/a[1]/span')
    terms=(By.XPATH,'//*[@id="root"]/div/div[3]/div/div[3]/a[2]/span')
    privacy=(By.XPATH,'//*[@id="root"]/div/div[3]/div/div[3]/a[3]/span')
    pass_mess = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/div/p')
    mail_mess = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[1]/div/p')
    invalid_mess = (By.XPATH, '//*[@id="client-snackbar"]/div')
    forgot_mail = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div/div/input')
    send_email = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]')

    def click_on_desired_element(self,elem):
        self.driver.find_element(*elem).click()

    def input_data_into_field(self, elem, data):
        self.driver.find_element(*elem).send_keys(data)

    def delete_field_data (self, elem):
        p = self.driver.find_element(*elem)
        p.send_keys(Keys.CONTROL + 'a')
        p.send_keys(Keys.BACK_SPACE)

    def show_invalid_message(self, elem):
        t = self.driver.find_element(*elem)
        e = t.text
        if t.is_displayed() == True:
            print(e)

    def element_is_visible(self,elem):
        t = self.driver.find_element(*elem)
        e = t.text
        if t.is_displayed() == True:
            print(e)



