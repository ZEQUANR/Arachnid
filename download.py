import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tools import operation_interval


def download_the_file(driver, element):
    download_button_xpath = '//*[@id="noticeDetail"]/div/div[1]/div[3]/div[1]/button'

    try:
        # 点击进入下载页面
        element.click()
        time.sleep(operation_interval(1.5))

        handles = driver.window_handles
        driver.switch_to.window(handles[1])

        WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, download_button_xpath))
        )
        time.sleep(operation_interval(2, 1))

        # 下载
        download_button = driver.find_element(By.XPATH, download_button_xpath)
        download_button.click()
        time.sleep(operation_interval(3))

        driver.close()
        driver.switch_to.window(handles[0])
        time.sleep(operation_interval(1.5))

    except Exception as e:
        return False

    return True
