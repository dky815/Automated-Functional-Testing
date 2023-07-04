from time import sleep

import allure

from common.mysql_operate import MysqlOperate
from page.LoginPage import LoginPage
from page.HomePage import HomePage
from logs.log import log


class TestMysqlConn:
    def test_mysql(self, driver):
        with allure.step("login"):
            LoginPage().login(driver, "william")
            sleep(3)

        with allure.step("get balance"):
            balance = HomePage().get_balance(driver)
            log.info(balance)

        with allure.step("get balance from db"):
            sql = "select balance from wallet where user_id=13;"
            db_balance = MysqlOperate().query(sql)[0][0]
            log.info(db_balance)

        with allure.step("Assert whether the data in the database is consistent with the page data"):
            assert str(balance) == str(db_balance)
