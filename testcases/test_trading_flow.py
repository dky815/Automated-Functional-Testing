from time import sleep

import pytest
import allure

from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage
from page.OrderPage import OrderPage
from page.TradingMarketPage import TradingMarketPage
from common.report_add_img import add_img_2_report
from common.tools import get_now_date_time_str


class TestTradingFlow:
    @pytest.mark.trading_flow
    @allure.feature("trading flow")
    @allure.description("trading flow")
    def test_trading_flow(self, driver):
        """trading flow"""
        with allure.step("login seller"):
            LoginPage().api_login(driver, "jay")
            add_img_2_report(driver, "login seller")

        with allure.step("enter add new goods"):
            LeftMenuPage().click_level_one_menu(driver, "产品")
            sleep(1)
            LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
            sleep(2)
            add_img_2_report(driver, "enter add new goods")

        with allure.step("add new goods"):
            goods_title = "test trading flow" + get_now_date_time_str()
            GoodsPage().add_new_goods(
                driver,
                goods_title=goods_title,
                goods_details="test trading flow",
                goods_num=1,
                goods_pic_list=["product_picture_1.jpg"],
                goods_price=99,
                goods_status="上架",
                bottom_button_name="提交"
            )
            add_img_2_report(driver, "add new goods")
            sleep(8)

        with allure.step("login buyer"):
            LoginPage().api_login(driver, "william")
            add_img_2_report(driver, "login buyer")

        with allure.step("enter trading market"):
            LeftMenuPage().click_level_one_menu(driver, "交易市场")
            add_img_2_report(driver, "enter trading market")

        with allure.step("search goods"):
            TradingMarketPage().input_search_input(driver, goods_title)
            TradingMarketPage().click_search(driver)
            add_img_2_report(driver, "search goods")

        with allure.step("click product card"):
            TradingMarketPage().click_product_card(driver, goods_title)
            sleep(1)
            add_img_2_report(driver, "click product card")

        with allure.step("click i want"):
            TradingMarketPage().click_i_want(driver)
            sleep(1)
            add_img_2_report(driver, "click i want")

        with allure.step("select address"):
            TradingMarketPage().click_address(driver)
            sleep(1)
            TradingMarketPage().select_detail_address(driver, 1)
            sleep(1)
            add_img_2_report(driver, "select address")

        with allure.step("click bottom button"):
            TradingMarketPage().click_bottom_button(driver)
            sleep(1)
            add_img_2_report(driver, "click bottom button")

        with allure.step("buyer pays"):
            OrderPage().click_order_operation(driver, goods_title, "去支付")
            sleep(1)
            OrderPage().click_order_operation_confirm(driver)
            add_img_2_report(driver, "buyer pays")

        with allure.step("login seller"):
            LoginPage().api_login(driver, "jay")
            add_img_2_report(driver, "login seller")

        with allure.step("enter sold goods"):
            LeftMenuPage().click_level_one_menu(driver, "我的订单")
            sleep(1)
            LeftMenuPage().click_level_two_menu(driver, "已卖出的宝贝")
            sleep(2)
            add_img_2_report(driver, "enter sold goods")

        with allure.step("seller shipped"):
            OrderPage().click_order_operation(driver, goods_title, "去发货")
            sleep(1)
            OrderPage().click_delivery_logistics(driver)
            sleep(1)
            OrderPage().click_select_logistics(driver, "顺丰速运")
            sleep(1)
            OrderPage().input_logistics_order_no(driver, "123456789")
            sleep(1)
            OrderPage().click_order_operation_confirm(driver)
            add_img_2_report(driver, "seller shipped")
            sleep(3)

        with allure.step("login buyer"):
            LoginPage().api_login(driver, "william")
            add_img_2_report(driver, "login buyer")

        with allure.step("enter purchased goods"):
            LeftMenuPage().click_level_one_menu(driver, "我的订单")
            sleep(1)
            LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
            sleep(2)
            add_img_2_report(driver, "enter purchased goods")

        with allure.step("buyer confirms receipt"):
            OrderPage().click_order_operation(driver, goods_title, "去确认收货")
            sleep(1)
            OrderPage().click_order_operation_confirm(driver)
            add_img_2_report(driver, "buyer confirms receipt")

        with allure.step("buyer evaluates"):
            OrderPage().click_order_operation(driver, goods_title, "去评价")
            sleep(1)
            OrderPage().click_evaluation(driver, 5)
            sleep(2)
            OrderPage().click_evaluation_confirm(driver)
            add_img_2_report(driver, "buyer evaluates")
