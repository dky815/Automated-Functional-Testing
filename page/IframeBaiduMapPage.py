from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.IframeBaiduMapBase import IframeBaiduMapBase


class IframeBaiduMapPage(IframeBaiduMapBase, ObjectMap):
    def get_baidu_map_search_button(self, driver):
        """
        get baidu map search button
        :param driver:
        :return:
        """
        button_xpath = self.search_button()
        return self.element_get(driver, By.XPATH, button_xpath)

    def switch_2_baidu_map_iframe(self, driver):
        """
        switch to baidu map iframe
        :param driver:
        :return:
        """
        iframe_xpath = self.baidu_map_iframe()
        return self.switch_into_iframe(driver, By.XPATH, iframe_xpath)

    def iframe_out(self, driver):
        """
        switch to trading system iframe from baidu map iframe
        :param driver:
        :return:
        """
        return self.switch_from_iframe_to_content(driver)
