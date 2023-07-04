import datetime
import os.path
import time

from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

from common.yaml_config import GetConf
from common.tools import get_project_path, sep
from common.find_img import FindImg
from common.report_add_img import add_img_path_2_report


class ObjectMap:
    # Get the base address
    url = GetConf().get_url()

    def element_get(self, driver, locate_type, locator_expression, timeout=10, must_be_visible=False):
        """
        Get a single element
        :param driver: browser driver
        :param locate_type: location method type
        :param locator_expression: locator expression
        :param timeout: timeout time
        :param must_be_visible: Whether the element must be visible, True must be visible, False is the default value
        :return: the returned element
        """
        # start time
        start_ms = time.time() * 1000
        # set end time
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            # lookup element
            try:
                element = driver.find_element(by=locate_type, value=locator_expression)
                # If the element is not necessarily visible, return the element directly
                if not must_be_visible:
                    return element
                # If the element must be visible, you need to determine whether the element is visible
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
            except Exception:
                now_ms = time.time() * 1000
                if now_ms >= stop_ms:
                    break
                pass
            time.sleep(0.1)
        raise ElementNotVisibleException("Element positioning failed, positioning method:" + locate_type + " Positioning expression:" + locator_expression)

    def wait_for_ready_state_complete(self, driver, timeout=30):
        """
        Wait for the page to fully load
        :param driver: browser driver
        :param timeout: timeout time
        :return:
        """
        # Starting time
        start_ms = time.time() * 1000
        # set end time
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            try:
                # Get the status of the page
                ready_state = driver.execute_script("return document.readyState")
            except WebDriverException:
                # If there is a driver error, the execution of js will fail, just skip it
                time.sleep(0.03)
                return True
            # Returns True if all page elements have been loaded
            if ready_state == "complete":
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000
                # break if timeout
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
        raise Exception("When opening the web page, the page elements are still not fully loaded after %s seconds" % timeout)

    def element_disappear(self, driver, locate_type, locator_expression, timeout=30):
        """
        Wait for page element to disappear
        :param driver: browser driver
        :param locate_type: location method type
        :param locator_expression: locator expression
        :param timeout: timeout time
        :return:
        """
        if locate_type:
            # Starting time
            start_ms = time.time() * 1000
            # set end time
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        now_ms = time.time() * 1000
                        if now_ms >= stop_ms:
                            break
                        time.sleep(0.1)
                except Exception:
                    return True
            raise Exception("The element does not disappear, the positioning method:" + locate_type + "\nPositioning expression:" + locator_expression)
        else:
            pass

    def element_appear(self, driver, locate_type, locator_expression, timeout=30):
        """
        Wait for page elements to appear
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param timeout:
        :return:
        """
        if locate_type:
            # Starting time
            start_ms = time.time() * 1000
            # set end time
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms >= stop_ms:
                        break
                    time.sleep(0.1)
                    pass
            raise ElementNotVisibleException("The element does not appear, the positioning method:" + locate_type + " Positioning expression:" + locator_expression)
        else:
            pass

    def element_to_url(
            self,
            driver,
            url,
            locate_type_disappear=None,
            locator_expression_disappear=None,
            locate_type_appear=None,
            locator_expression_appear=None
    ):
        """
        jump address
        :param driver: browser driver
        :param url: redirect URL
        :param locate_type_disappear: The positioning method to wait for the page element to disappear
        :param locator_expression_disappear: The locator expression that waits for the page element to disappear
        :param locate_type_appear: Waiting for the positioning method of the page element to appear
        :param locator_expression_appear: The locator expression that waits for the page element to appear
        :return:
        """
        try:
            driver.get(self.url + url)
            # Wait for all page elements to load
            self.wait_for_ready_state_complete(driver)
            # Wait for the element to disappear after jumping to the address
            self.element_disappear(
                driver,
                locate_type_disappear,
                locator_expression_disappear
            )
            # Wait for the element to appear after jumping to the address
            self.element_appear(
                driver,
                locate_type_appear,
                locator_expression_appear
            )
        except Exception as e:
            print("The jump address is abnormal, the reason for the exception:%s" % e)
            return False
        return True

    def element_is_display(self, driver, locate_type, locator_expression):
        """
        Whether the element is displayed
        :param driver:
        :param locate_type:
        :param locator_expression:
        :return:
        """
        try:
            driver.find_element(by=locate_type, value=locator_expression)
            return True
        except NoSuchElementException:
            # A NoSuchElementException occurred, indicating that the element was not found on the page, and returns False
            return False

    def element_fill_value(self, driver, locate_type, locator_expression, fill_value, timeout=30):
        """
        Element value
        :param driver: browser driver
        :param locate_type: location method
        :param locator_expression: locator expression
        :param fill_value: filled value
        :param timeout: timeout time
        :return:
        """
        # element must appear before
        element = self.element_appear(
            driver,
            locate_type=locate_type,
            locator_expression=locator_expression,
            timeout=timeout
        )
        try:
            # First clear the original value in the element
            element.clear()
        except StaleElementReferenceException:  # The page element is not refreshed, and the element is captured, which triggers this exception
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(
                driver,
                locate_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout
            )
            try:
                element.clear()
            except Exception:
                pass
        except Exception:
            pass
        # The filled value is converted into a string
        if type(fill_value) is int or type(fill_value) is float:
            fill_value = str(fill_value)
        try:
            # The filled value does not end with \n
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(driver, locate_type=locate_type, locator_expression=locator_expression)
            element.clear()
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except Exception:
            raise Exception("Failed to fill element value")

        return True

    def element_click(
            self,
            driver,
            locate_type,
            locator_expression,
            locate_type_disappear=None,
            locator_expression_disappear=None,
            locate_type_appear=None,
            locator_expression_appear=None,
            timeout=30
    ):
        """
        element click
        :param driver: browser driver
        :param locate_type: location method type
        :param locator_expression: locator expression
        :param locate_type_disappear: the type of location method to wait for the element to disappear
        :param locator_expression_disappear: The locator expression that waits for the element to disappear
        :param locate_type_appear: The type of positioning method to wait for the element to appear
        :param locator_expression_appear: The locator expression that waits for the element to appear
        :param timeout: timeout time
        :return:
        """
        # element to be visible
        element = self.element_appear(
            driver=driver,
            locate_type=locate_type,
            locator_expression=locator_expression,
            timeout=timeout
        )
        try:
            # click element
            element.click()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(
                driver=driver,
                locate_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout
            )
            element.click()
        except Exception as e:
            print("There is an exception on the page, and the element cannot be clicked", e)
            return False
        try:
            # The element appears or disappears after the element is clicked
            self.element_appear(
                driver,
                locate_type_appear,
                locator_expression_appear
            )
            self.element_disappear(
                driver,
                locate_type_disappear,
                locator_expression_disappear
            )
        except Exception as e:
            print("Wait for element to disappear or fail", e)
            return False

        return True

    def upload(self, driver, locate_type, locator_expression, file_path):
        """
        upload file
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param file_path:
        :return:
        """
        element = self.element_get(driver, locate_type, locator_expression)
        return element.send_keys(file_path)

    def switch_into_iframe(self, driver, locate_iframe_type, locate_iframe_expression):
        """
        switch into iframe
        :param driver: browser driver
        :param locate_iframe_type: the way to locate iframe
        :param locate_iframe_expression: expression to locate iframe
        :return:
        """
        iframe = self.element_get(driver, locate_iframe_type, locate_iframe_expression)
        driver.switch_to.frame(iframe)

    def switch_from_iframe_to_content(self, driver):
        """
        Switch back to main page from iframe
        :param driver:
        :return:
        """
        driver.switch_to.parent_frame()

    def switch_window_2_latest_handle(self, driver):
        """
        Handle to switch windows to the latest window
        :param driver:
        :return:
        """
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])

    def find_img_in_source(self, driver, img_name):
        """
        Take screenshots and find images in screenshots
        :param driver:
        :param img_name:
        :return:
        """
        # The path to save the picture after taking a screenshot
        source_img_path = get_project_path() + sep(["img", "source_img", img_name], add_sep_before=True)
        print("source_img_path:", source_img_path)
        # The path of the image to be found
        search_img_path = get_project_path() + sep(["img", "assert_img", img_name], add_sep_before=True)
        print("search_img_path:", search_img_path)
        # Take a screenshot and save the image
        driver.get_screenshot_as_file(source_img_path)
        time.sleep(3)
        add_img_path_2_report(source_img_path, "original image")
        add_img_path_2_report(search_img_path, "image to find")
        # Find whether there is a specified image in the original image, and return the confidence value
        confidence = FindImg().get_confidence(source_img_path, search_img_path)
        return confidence

    def element_screenshot(self, driver, locate_type, locator_expression):
        """
        element screenshot
        :param driver:
        :param locate_type:
        :param locator_expression:
        :return:
        """
        ele_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        ele_img_dir_path = get_project_path() + sep(["img", "ele_img"], add_sep_before=True, add_sep_after=True)
        if not os.path.exists(ele_img_dir_path):
            os.mkdir(ele_img_dir_path)
        ele_img_path = ele_img_dir_path + ele_name
        self.element_get(driver, locate_type, locator_expression).screenshot(ele_img_path)
        return ele_img_path

    def scroll_to_element(self, driver, locate_type, locator_expression):
        """
        scroll to element
        :param driver:
        :param locate_type:
        :param locator_expression:
        :return:
        """
        ele = self.element_get(driver, locate_type, locator_expression)
        driver.execute_script("arguments[0].scrollIntoView()", ele)
        return True
