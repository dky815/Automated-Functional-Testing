from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.IframeImoocBase import IframeImoocBase
from logs.log import log


class IframeImoocPage(IframeImoocBase, ObjectMap):
    def get_imooc_logo_img(self, driver):
        """
        get imooc logo img
        :param driver:
        :return:
        """
        log.info("get imooc logo img")
        img_xpath = self.imooc_logo()
        return self.element_get(driver, By.XPATH, img_xpath)

    def switch_2_imooc_iframe(self, driver):
        """
        switch to imooc iframe
        :param driver:
        :return:
        """
        log.info("switch to imooc iframe")
        iframe_xpath = self.imooc_iframe()
        return self.switch_into_iframe(driver, By.XPATH, iframe_xpath)

    def iframe_out(self, driver):
        """
        switch to trading system iframe from imooc iframe
        :param driver:
        :return:
        """
        log.info("switch to trading system iframe from imooc iframe")
        return self.switch_from_iframe_to_content(driver)
