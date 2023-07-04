from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from common.tools import get_project_path, sep


class DriverConfig:
    def driver_config(self):
        """
        browser driver
        :return:
        """
        options = webdriver.ChromeOptions()
        # Set the window size, set it to 1920*1080
        options.add_argument("window-size=1920,1080")
        # remove the automation info
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # Solve the problem that selenium cannot access https website
        options.add_argument("--ignore-certificate-errors")
        # allow insecure localhost
        options.add_argument("--allow-insecure-localhost")
        # set to incognito mode
        options.add_argument("--incognito")
        # set to headless mode
        # options.add_argument("--headless")
        # Solve screen lag
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(ChromeDriverManager(cache_valid_range=365).install(),
                                  options=options)
        # delete all cookies
        driver.delete_all_cookies()

        return driver
