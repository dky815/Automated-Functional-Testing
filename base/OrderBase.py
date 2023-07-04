class OrderBase:
    def order_tab(self, tab_name):
        """
        order tab button
        :param tab_name: All, pending payment, pending shipment, in transit, pending confirmation, pending evaluation
        :return:
        """
        return "//div[@role='tab' and text()='" + tab_name + "']"

    def order_operation(self, product_title, operation):
        """
        Action buttons for orders
        :param product_title:
        :param operation:
        :return:
        """
        return "//div[text()='" + product_title + "']/ancestor::tr//span[text()='" + operation + "']/parent::button"

    def order_operation_confirm(self):
        """
        After clicking the operation button, the OK button of the pop-up box
        :return:
        """
        return "//div[@class='el-dialog__wrapper' and contains(@style,'index')]//span[text()='确 定']/parent::button"

    def delivery_logistics(self):
        """
        Delivery logistics company selection box
        :return:
        """
        return "//label[text()='物流公司']/following-sibling::div//input"

    def select_logistics(self, company):
        """
        logistics company
        :param company:
        :return:
        """
        return "//span[text()='" + company + "']/parent::li"

    def logistics_order_no(self):
        """
        shipment number
        :return:
        """
        return "//label[text()='物流单号']/following-sibling::div//input"

    def evaluation(self, num):
        """
        rating star
        :param num:
        :return:
        """
        return "//span[text()='请给卖家评价']/following-sibling::div/span[" + str(num) + "]/i"

    def evaluation_confirm(self):
        """
        OK after evaluation
        :return:
        """
        return "//span[text()='评价']/ancestor::div[@role='dialog']//span[text()='确 定']/parent::button"
