from sample_project.utilities_files import config_pro as cs
from selenium.webdriver.common.by import By
import time as tt
class logdata:
    tu=cs.red()
    credintails={'user':tu.user(),
                 'password':tu.password(),
                 }
    user_input_id=tu.uesr_password_id()
    user_password_id=tu.uesr_password_id()
    login_but=r"//*[contain(text(),'Log in')]"
    @staticmethod
    def ping():
        return tt.sleep(5)
    def __init__(self,drive):
        # driver
        self.ck=drive
        self.ck.get(url='https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
    
    def login_data(self):
        try:
            self.ma=self.ck
            self.ma.set_page_load_timeout(25)
            self.ma.maximize_window()
            self.id=self.ma.find_element(By.NAME,logdata.user_input_id)

            self.id.clear()
            self.ping()
            self.id.send_keys(logdata.credintails['user'])
            self.id=self.ma.find_element(By.NAME,self.user_password_id)
            self.id.clear()
            self.ping()
            self.id.send_keys(logdata.credintails['password'])
            self.ma.find_element(By.XPATH,self.login_but).click()
        except Exception:
            self.ck.get_screenshot_as_file(r'D:\testing_pro1\project_level\sample_project\reports\screenshots\failure.png')
           
            

    def log_out(self):
        self.ping()
        self.ma.find_element(By.XPATH,"//*[contains(text(),'Logout')]").click()
        self.ma.quit()
        


cv="failure.png"