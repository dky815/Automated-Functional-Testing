import pytest

from config.driver_config import DriverConfig
from common.report_add_img import add_img_2_report



@pytest.fixture()
def driver():
    global get_driver
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Get the call result of the hook method
    out = yield
    # Get the test report from the call result of the hook method
    report = out.get_result()
    report.description = str(item.function.__doc__)

    if report.when == "call":
        if report.failed:
            # take screenshot if test case failure
            add_img_2_report(get_driver, "failure screenshot", need_sleep=False)
