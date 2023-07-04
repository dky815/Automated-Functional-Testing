class GoodsBase:
    def goods_title(self):
        """
        product title
        :return:
        """
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品标题']"

    def goods_details(self):
        """
        product details
        :return:
        """
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品详情']"

    def goods_num(self, plus=True):
        """
        Number of Products
        :param plus: If it is True, use the plus sign, if it is False, enter the quantity directly
        :return:
        """
        if plus:
            return "//label[@for='product_stock']/following-sibling::div//i[@class='el-icon-plus']/parent::span"
        else:
            return "//label[@for='product_stock']/following-sibling::div//input[@placeholder='商品数量']"

    def goods_img(self):
        """
        product picture
        :return:
        """
        return "//input[@type='file']"

    def goods_price(self):
        """
        Commodity price
        :return:
        """
        return "//form[@class='el-form']//input[@placeholder='请输入商品单价']"

    def goods_status(self):
        """
        commodity status
        :return:
        """
        return "//form[@class='el-form']//input[@placeholder='请选择商品状态']"

    def goods_status_select(self, select_name):
        """
        Select product status
        :param select_name: put it on the shelf, or take it off the shelf
        :return:
        """
        return "//span[text()='" + select_name + "']/parent::li"

    def add_goods_bottom_button(self, button_name):
        """
        Add second-hand goods bottom button
        :param button_name:
        :return:
        """
        return "//span[text()='" + button_name + "']/parent::button"
