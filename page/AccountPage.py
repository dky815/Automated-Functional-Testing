from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.AccountBase import AccountBase
from common.tools import get_img_path


class AccountPage(AccountBase, ObjectMap):
    def upload_avatar(self, driver, img_name):
        """
        upload profile picture
        :param driver:
        :param img_name:
        :return:
        """
        img_path = get_img_path(img_name)
        upload_xpath = self.basic_info_avatar_input()
        return self.upload(driver, By.XPATH, upload_xpath, img_path)

    def click_save(self, driver):
        """
        Profile - click to save
        :param driver:
        :return:
        """
        button_xpath = self.basic_info_save_button()
        return self.element_click(driver, By.XPATH, button_xpath)
