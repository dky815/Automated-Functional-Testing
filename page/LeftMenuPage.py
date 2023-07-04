from selenium.webdriver.common.by import By

from base.LeftMenuBase import LeftMenuBase
from base.ObjectMap import ObjectMap


class LeftMenuPage(LeftMenuBase, ObjectMap):

    def click_level_one_menu(self, driver, menu_name):
        """
        click level one menu
        :param driver:
        :param menu_name:
        :return:
        """
        menu_xpath = self.level_one_menu(menu_name)
        return self.element_click(driver, By.XPATH, menu_xpath)

    def click_level_two_menu(self, driver, menu_name):
        """
        click level two menu
        :param driver:
        :param menu_name:
        :return:
        """
        menu_xpath = self.level_two_menu(menu_name)
        return self.element_click(driver, By.XPATH, menu_xpath)
