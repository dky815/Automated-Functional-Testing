class AccountBase:
    def basic_info_avatar_input(self):
        """
        Basic Information-Personal Avatar
        :return:
        """
        return "//input[@type='file']"

    def basic_info_save_button(self):
        """
        Basic Information - Save Button
        :return:
        """
        return "//span[text()='保存']/parent::button"
