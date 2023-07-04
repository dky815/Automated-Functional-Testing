from time import sleep

import pytest
import allure

from page.LoginPage import LoginPage
from common.report_add_img import add_img_2_report


class TestLoginAssert:
    @pytest.mark.login
    @allure.feature("login")
    @allure.description("assert image after login")
    def test_login_assert(self, driver):
        """assert image after login"""
        with allure.step("login"):
            LoginPage().login(driver, "william")
            sleep(3)
            add_img_2_report(driver, "login")

        with allure.step("assert image"):
            assert LoginPage().login_assert(driver, "head_img.png") > 0.9
