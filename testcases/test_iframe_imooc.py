from time import sleep

import pytest
import allure

from common.report_add_img import add_img_2_report
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.IframeImoocPage import IframeImoocPage


class TestIframeImooc:
    @pytest.mark.iframe
    @allure.feature("iframe test")
    @allure.description("iframe test")
    def test_iframe_imooc(self, driver):
        """iframe test"""
        with allure.step("login"):
            LoginPage().login(driver, "william")
            sleep(3)
            add_img_2_report(driver, "login")

        with allure.step("switch to iframe test"):
            LeftMenuPage().click_level_one_menu(driver, "iframe测试")
            sleep(1)
            IframeImoocPage().switch_2_imooc_iframe(driver)
            add_img_2_report(driver, "switch to iframe test")

        with allure.step("get logo element"):
            IframeImoocPage().get_imooc_logo_img(driver)
            add_img_2_report(driver, "get logo element")

        with allure.step("switch out iframe"):
            IframeImoocPage().iframe_out(driver)
            sleep(3)
            add_img_2_report(driver, "switch out iframe")

        with allure.step("click home page"):
            LeftMenuPage().click_level_one_menu(driver, "首页")
            sleep(3)
            add_img_2_report(driver, "click home page")
