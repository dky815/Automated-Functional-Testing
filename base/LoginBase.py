class LoginBase:

    def login_input(self, input_placeholder):
        """
        Login user name, password input box
        :param input_placeholder:
        :return:
        """
        return "//input[@placeholder='" + input_placeholder + "']"

    def login_button(self, button_name):
        """
        login button
        :param button_name:
        :return:
        """
        return "//span[text()='" + button_name + "']/parent::button"

    def login_success(self):
        """
        Login successful prompt
        :return:
        """
        return "//p[text()='登录成功']"

    def need_captcha(self):
        """
        Checkbox for verification code
        :return:
        """
        return "//span[contains(text(),'是否需要验证码')]/preceding-sibling::span/span"

    def captcha(self):
        """
        captcha
        :return:
        """
        return "//div[@class='el-image']"

    def input_captcha(self):
        """
        Input box for captcha
        :return:
        """
        return "//input[@placeholder='请输入验证码']"
