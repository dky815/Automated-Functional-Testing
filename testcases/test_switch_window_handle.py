from time import sleep

import allure

from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from common.report_add_img import add_img_2_report


class TestWindowHandle:
    @allure.description("window handle test")
    @allure.epic("window handle epic")
    @allure.feature("window handle feature")
    @allure.story("window handle story")
    @allure.tag("window handle tag")
    def test_switch_window_handles(self, driver):
        with allure.step("login"):
            LoginPage().login(driver, "jay")
            sleep(3)
            add_img_2_report(driver, "login")

        with allure.step("click external link"):
            LeftMenuPage().click_level_one_menu(driver, "外链")
            sleep(1)
            add_img_2_report(driver, "click external link")

        with allure.step("assert external link page title"):
            title = ExternalLinkPage().goto_imooc(driver)
            print("title:", title)
            assert title == "慕课网-程序员的梦工厂"
