from time import sleep

import pytest
import allure

from common.report_add_img import add_img_2_report
from page.LoginPage import LoginPage


class TestCaptchaLogin:
    @pytest.mark.login
    @allure.feature("login")
    @allure.description("captcha login")
    def test_captcha_login(self, driver):
        """captcha login"""
        with allure.step("login"):
            LoginPage().login(driver, "jay", need_captcha=True)
            sleep(3)
            add_img_2_report(driver, "login")
