from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import os

from facebook.driver import Selenium
from facebook.driver.firefox.download import download_driver

class FirefoxDriver(Selenium):
    def get_options(self):
        firefoxProfile = webdriver.FirefoxProfile(self.cookie_dir)

        
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        firefoxProfile.set_preference("media.volume_scale", "0.0")
        
        # options = Options()
        # options.add_argument("--disable-notifications")
        # options.add_argument("--disable-infobars")
        # options.add_argument("--mute-audio")
        # options.add_argument("--start-maximized")
        # options.add_argument('user-data-dir={}'.format(self.cookie_dir))
        
        # options.add_argument("--headless")
        # options.setBinary("/path/to/other/chrome/binary")
        # options.headless = True
        return firefoxProfile
    
    def init_selenium(self):
        download_driver()
        try:
            os.makedirs(self.cookie_dir)
        except:
            pass
        firefoxProfile = self.get_options()
        try:
            executable_path = os.path.join(os.getcwd(), 'geckodriver')
            self.driver = webdriver.Firefox(firefoxProfile, executable_path=executable_path)
        except Exception as e:
            self.quit(True)