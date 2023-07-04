from time import sleep

import allure
import pytest

from page.LoginPage import LoginPage
from common.report_add_img import add_img_2_report


class TestLogin:
    @pytest.mark.login
    @allure.feature("login")
    @allure.description("login")
    def test_login(self, driver):
        """Login with wrong account"""
        with allure.step("login"):
            LoginPage().login(driver, "failure")
            sleep(3)
            add_img_2_report(driver, "login")
