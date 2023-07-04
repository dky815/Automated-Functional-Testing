from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.OrderBase import OrderBase
from logs.log import log


class OrderPage(OrderBase, ObjectMap):
    def click_order_tab(self, driver, tab_name):
        """
        click order tab
        :param driver:
        :param tab_name:
        :return:
        """
        tab_xpath = self.order_tab(tab_name)
        return self.element_click(driver, By.XPATH, tab_xpath)

    def click_order_operation(self, driver, product_title, operation):
        """
        click order operation button
        :param driver:
        :param product_title:
        :param operation:
        :return:
        """
        log.info("product title: " + product_title + ", click order operation button" + operation)
        button_xpath = self.order_operation(product_title, operation)
        return self.element_click(driver, By.XPATH, button_xpath)

    def click_order_operation_confirm(self, driver):
        """
        click order operation confirm button
        :param driver:
        :return:
        """
        log.info("click order operation confirm button")
        button_xpath = self.order_operation_confirm()
        return self.element_click(driver, By.XPATH, button_xpath)

    def click_delivery_logistics(self, driver):
        """
        click delivery logistics
        :param driver:
        :return:
        """
        log.info("click delivery logistics")
        input_xpath = self.delivery_logistics()
        return self.element_click(driver, By.XPATH, input_xpath)

    def click_select_logistics(self, driver, company):
        """
        click select logistics
        :param driver:
        :param company:
        :return:
        """
        log.info("click select logistics")
        select_xpath = self.select_logistics(company)
        return self.element_click(driver, By.XPATH, select_xpath)

    def input_logistics_order_no(self, driver, order_no):
        """
        input logistics order no
        :param driver:
        :param order_no:
        :return:
        """
        log.info("input logistics order no: " + str(order_no))
        input_xpath = self.logistics_order_no()
        return self.element_fill_value(driver, By.XPATH, input_xpath, order_no)

    def click_evaluation(self, driver, num):
        """
        click evaluation star
        :param driver:
        :param num:
        :return:
        """
        log.info("evaluation: " + str(num) + " star")
        star_xpath = self.evaluation(num)
        return self.element_click(driver, By.XPATH, star_xpath)

    def click_evaluation_confirm(self, driver):
        """
        click evaluation confirm
        :param driver:
        :return:
        """
        log.info("click evaluation confirm")
        button_xpath = self.evaluation_confirm()
        return self.element_click(driver, By.XPATH, button_xpath)
