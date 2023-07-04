from time import sleep

import allure


def add_img_2_report(driver, step_name, need_sleep=True):
    """
    Screenshot and insert allure report
    :param driver:
    :param step_name:
    :param need_sleep:
    :return:
    """
    if need_sleep:
        sleep(2)
    allure.attach(
        driver.get_screenshot_as_png(),
        step_name + ".png",
        allure.attachment_type.PNG
    )


def add_img_path_2_report(img_path, step_name):
    """
    Insert image into Allure report
    :param img_path: image path
    :param step_name: step name
    :return:
    """
    allure.attach.file(img_path, step_name, allure.attachment_type.PNG)
