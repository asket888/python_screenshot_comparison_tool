from os import path

from selenium import webdriver
from selenium.webdriver import chrome
from webdriver_manager.chrome import ChromeDriverManager

from utils.config_util import get_env


class Driver:

    _IMPLICIT_TIMEOUT = 10

    def __init__(self, env):
        self.env = get_env(env=env)
        self.driver = self.get_driver()
        self.driver.implicitly_wait(self._IMPLICIT_TIMEOUT)

    def get_driver(self):
        options = chrome.options.Options()
        options.add_argument("--window-size=800x4800")
        options.headless = True
        return webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                chrome_options=options)

    def clean_up(self):
        self.driver.quit()

    def get_page(self, url):
        self.driver.get(url)

    def make_screenshot(self, file_name):
        page = self.driver.find_element_by_tag_name("body")
        page.screenshot(path.join(path.dirname(path.dirname(path.realpath(__file__))), "screenshots/actual", file_name))
