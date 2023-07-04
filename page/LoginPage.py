import time

import requests
from selenium.webdriver.common.by import By

from base.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConf
from logs.log import log
from common.report_add_img import add_img_path_2_report
from common.ocr_identify import OcrIdentify


class LoginPage(LoginBase, ObjectMap):

    def login_input_value(self, driver, input_placeholder, input_value):
        """
        login input value
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        """
        log.info("input" + input_placeholder + "is: " + str(input_value))
        input_xpath = self.login_input(input_placeholder)
        # return driver.find_element_by_xpath(input_xpath).send_keys(input_value)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)

    def click_login(self, driver, button_name):
        """
        click login
        :param driver:
        :param button_name:
        :return:
        """
        log.info("click login")
        button_xpath = self.login_button(button_name)
        # return driver.find_element_by_xpath(button_xpath).click()
        return self.element_click(driver, By.XPATH, button_xpath)

    def login(self, driver, user, need_captcha=False):
        """
        login
        :param driver:
        :param user:
        :param need_captcha:
        :return:
        """
        log.info("go to login page")
        self.element_to_url(driver, "/login")
        if need_captcha:
            time.sleep(3)
            log.info("need captcha")
            self.select_need_captcha(driver)
            captcha_xpath = self.captcha()
            ele_img_path = self.element_screenshot(driver, By.XPATH, captcha_xpath)
            add_img_path_2_report(ele_img_path, "image captcha")
            identify = OcrIdentify().identify(ele_img_path)
            log.info("captcha is " + str(identify))
            input_captcha_xpath = self.input_captcha()
            log.info("input captcha")
            self.element_fill_value(driver, By.XPATH, input_captcha_xpath, identify)
            time.sleep(3)
        username, password = GetConf().get_username_password(user)
        self.login_input_value(driver, "用户名", username)
        self.login_input_value(driver, "密码", password)
        self.click_login(driver, "登录")
        self.assert_login_success(driver)

    def api_login(self, driver, user):
        """
        login by api
        :param driver:
        :param user:
        :return:
        """
        log.info("go to login page")
        self.element_to_url(driver, "/login")
        username, password = GetConf().get_username_password(user)
        log.info("username: " + str(username))
        log.info("password: " + str(password))
        url = GetConf().get_url()
        data = {
            "user": username,
            "password": password
        }
        log.info("login by api")
        res = requests.post(url + "/api/user/login", json=data)
        token = res.json()["data"]["token"]
        js_script = "window.sessionStorage.setItem('token','%s');" % token
        log.info("write token to session")
        driver.execute_script(js_script)
        time.sleep(2)
        log.info("go to home page")
        self.element_to_url(driver, "/")

    def login_assert(self, driver, img_name):
        """
        assert profile picture after login
        :param driver:
        :param img_name:
        :return:
        """
        log.info("assert profile picture after login")
        return self.find_img_in_source(driver, img_name)

    def assert_login_success(self, driver):
        """
        assert login success
        :param driver:
        :return:
        """
        success_xpath = self.login_success()
        self.element_appear(driver, By.XPATH, success_xpath, timeout=2)

    def select_need_captcha(self, driver):
        """
        select need captcha
        :param driver:
        :return:
        """
        log.info("click need captcha")
        select_xpath = self.need_captcha()
        return self.element_click(driver, By.XPATH, select_xpath)
