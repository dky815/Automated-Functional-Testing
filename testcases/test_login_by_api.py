from time import sleep

import pytest
import allure

from page.LoginPage import LoginPage


class TestLoginByApi:
    @pytest.mark.login
    @allure.feature("login by api")
    @allure.description("login by api")
    def test_login_by_api(self, driver):
        """login by api"""
        with allure.step("login jay"):
            LoginPage().api_login(driver, "jay")
            sleep(5)

        with allure.step("switch to william user"):
            LoginPage().api_login(driver, "william")
            sleep(5)
