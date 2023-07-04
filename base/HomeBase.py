class HomeBase:
    def wallet_switch(self):
        """
        Home Wallet Switch
        :return:
        """
        return "//span[contains(@class,'switch')]"

    def logo(self):
        """
        After entering the system, the logo on the upper left corner of the homepage
        :return:
        """
        return "//div[contains(text(),'二手')]"

    def welcome(self):
        """
        Home, welcome back
        :return:
        """
        return "//span[starts-with(text(),'欢迎您回来')]"

    def show_date(self):
        """
        The first page shows the date
        :return:
        """
        return "//div[text()='我的日历']/following-sibling::div"

    def home_user_avatar(self):
        """
        Big picture of user avatar on the home page
        :return:
        """
        return "//span[contains(text(),'欢迎您回来')]/parent::div/preceding-sibling::div//img"

    def home_user_avatar_2(self):
        """
        Large picture of home page user profile picture 2
        :return:
        """
        return "//span[text()='我的地址']/ancestor::div[@class='first_card']/div[contains(@class,'avatar')]//img"

    def user_balance(self):
        """
        Home-Account Balance
        :return:
        """
        return "//th[text()='账户余额']/parent::tr/following-sibling::tr/td[1]"
