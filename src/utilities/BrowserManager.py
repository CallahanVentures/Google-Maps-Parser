from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import os

class BrowserManager:
    @staticmethod
    def initialize_browser():
        options = webdriver.ChromeOptions()
        options.add_argument("--log-level=3")
        options.add_experimental_option("prefs", {"download.default_directory": os.getcwd() + "/"})
        try:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            driver.set_window_position(0, 1920)
            return driver
        except Exception as e:
            print("There Was An Error While Initializing Browser")
            print(e)
            exit()
