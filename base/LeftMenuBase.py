class LeftMenuBase:

    def level_one_menu(self, menu_name):
        """
        first level menu bar
        :param menu_name: menu bar name
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/ancestor::li"

    def level_two_menu(self, menu_name):
        """
        second level menu bar
        :param menu_name: menu bar name
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/parent::li"
