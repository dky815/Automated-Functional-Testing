from time import sleep

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.TradingMarketBase import TradingMarketBase
from logs.log import log


class TradingMarketPage(TradingMarketBase, ObjectMap):
    def input_search_input(self, driver, input_value):
        """
        Enter the search product input box
        :param driver:
        :param input_value:
        :return:
        """
        log.info("Enter the search product input box" + input_value)
        search_input_xpath = self.search_input()
        return self.element_fill_value(driver, By.XPATH, search_input_xpath, input_value)

    def click_search(self, driver):
        """
        click search button
        :param driver:
        :return:
        """
        log.info("click search button")
        search_xpath = self.search()
        return self.element_click(driver, By.XPATH, search_xpath)

    def click_product_card(self, driver, product_name):
        """
        click product card
        :param driver:
        :param product_name:
        :return:
        """
        log.info("click" + product_name + "product card")
        product_card_xpath = self.product_card(product_name)
        return self.element_click(driver, By.XPATH, product_card_xpath)

    def click_i_want(self, driver):
        """
        click i want button
        :param driver:
        :return:
        """
        log.info("click i want button")
        i_want_button_xpath = self.i_want_button()
        self.scroll_to_element(driver, By.XPATH, i_want_button_xpath)
        return self.element_click(driver, By.XPATH, i_want_button_xpath)

    def click_address(self, driver):
        """
        click address
        :param driver:
        :return:
        """
        log.info("click address")
        receive_xpath = self.receive_address()
        return self.element_click(driver, By.XPATH, receive_xpath)

    def select_detail_address(self, driver, num, address=None):
        """
        select detail address
        :param driver:
        :param num:
        :param address:
        :return:
        """
        if address:
            log.info("select detail address" + address)
            address_xpath = self.receive_address_detail(0, address=address)
        else:
            log.info("select the " + str(num) + " address")
            address_xpath = self.receive_address_detail(num)
        return self.element_click(driver, By.XPATH, address_xpath)

    def click_bottom_button(self, driver):
        """
        click bottom button
        :param driver:
        :return:
        """
        log.info("click bottom button")
        button_xpath = self.bottom_confirm()
        return self.element_click(driver, By.XPATH, button_xpath)
