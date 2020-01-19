from facebook.driver import Selenium
from selenium.webdriver.firefox.options import Options
from facebook.driver.firefox.download import download_driver

class FirefoxDriver(Selenium):
    def get_options(self):
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        options.add_argument("--start-maximized")
        options.add_argument('user-data-dir={}'.format(self.cookie_dir))
        
        # options.add_argument("--headless")
        # options.setBinary("/path/to/other/chrome/binary")
        # options.headless = True
        return options
    
    def init_selenium(self):
        download_driver()
        options = self.get_options()
        try:
            self.driver = webdriver.Chrome(executable_path=executable_path, options=options)
        except Exception as e:
            self.quit(True)