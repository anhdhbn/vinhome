from easydict import EasyDict as edict
from pathlib import Path
import os, sys
from facebook.driver.firefox import FirefoxDriver
from facebook.driver.chrome import ChromeDriver
from facebook.constant import constant

from dotenv import load_dotenv
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

TYPE_DRIVER = os.getenv("TYPE_DRIVER")
EMAIL_FB = os.getenv("EMAIL_FB")
PASS_FB = os.getenv("PASS_FB")

app = edict({
    'email_fb': EMAIL_FB,
    'pass_fb': PASS_FB,
    'type_driver': FirefoxDriver if TYPE_DRIVER == "0" else ChromeDriver
})

class Driver(app.type_driver):
    def __init__(self, iduser, password):
        self.iduser = iduser
        self.password = password
        self.cookie_dir = os.path.join(os.getcwd(), "cookies", iduser)
        self.driver = None
        self.init_selenium()
        self.timeout_second = 30

    def login(self):
        self.driver.get("https://facebook.com")
        if constant.word_checklogin in self.driver.page_source: return True 
        try:
            self.driver.find_element_by_name('email').send_keys(self.email)
            self.driver.find_element_by_name('pass').send_keys(self.password)
            self.driver.find_element_by_id('loginbutton').click()
            if constant.word_checklogin in self.driver.page_source: return True
        except Exception as e:
            print(e.with_traceback())
            print("There's some error in log in.")
            print(sys.exc_info()[0])
            self.quit()

        if constant.word_checklogin in self.driver.page_source: return True
        else: return False

        # mfa_code_input = self.safe_get_element_by_id('approvals_code')

        # if mfa_code_input is not None:
        #     mfa_code_input.send_keys(input("Enter MFA code: "))
        #     self.driver.find_element_by_id('checkpointSubmitButton').click()

        #     # there are so many screens asking you to verify things. Just skip them all
        #     while self.safe_get_element_by_id('checkpointSubmitButton') is not None:
        #         dont_save_browser_radio = self.safe_get_element_by_id('u_0_3')
        #         if dont_save_browser_radio is not None:
        #             dont_save_browser_radio.click()

        #         self.driver.find_element_by_id('checkpointSubmitButton').click()

        # if constant.word_checklogin not in self.driver.page_source:
        #     self.quit()
        #     return False
        # else: 
        #     return True