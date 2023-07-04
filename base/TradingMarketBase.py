class TradingMarketBase:
    def search_input(self):
        """
        Search product input box
        :return:
        """
        return "//div[text()='搜索宝贝']/following-sibling::input"

    def search(self):
        """
        search button
        :return:
        """
        return self.search_input() + "/following-sibling::div/button"

    def product_card(self, product_name):
        """
        product card
        :param product_name: product name
        :return:
        """
        return "//div[text()='" + product_name + "']/ancestor::div[@class='el-card__body']"

    def i_want_button(self):
        """
        i want button
        :return:
        """
        return "//span[text()='我想要']/parent::button"

    def receive_address(self):
        """
        receive address
        :return:
        """
        return "//input[@placeholder='收货地址']"

    def receive_address_detail(self, num, address=None):
        """
        receive address detail
        :param num:
        :param address:
        :return:
        """
        if address:
            return "//span[text()='" + address + "']/parent::li"
        else:
            return "//ul[contains(@class,'list')]/li[" + str(num) + "]"

    def bottom_confirm(self):
        """
        bottom confirm button
        :return:
        """
        return "//span[text()='确 定']/parent::button"
