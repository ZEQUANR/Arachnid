import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tools import operation_interval
from download import download_the_file


def filter_by_date(driver, date):
    # 开始日期输入框
    start_date_input_xpath = (
        '//*[@id="main"]/div[2]/div[1]/div[2]/div/div[2]/form/div[1]/div/div/input[1]'
    )

    try:
        start_date_input = driver.find_element(By.XPATH, start_date_input_xpath)

        for i in date:
            start_date_input.send_keys(i)
            time.sleep(operation_interval(0.5))

        l = len(date)
        for _ in range(l):
            start_date_input.send_keys(Keys.ARROW_LEFT)
            time.sleep(operation_interval(0.5))

        for _ in range(10):  # 10 is date len
            start_date_input.send_keys(Keys.BACKSPACE)
            time.sleep(operation_interval(0.5))

        time.sleep(operation_interval(1))

        start_date_input.send_keys(Keys.ENTER)

        time.sleep(operation_interval(1))

    except Exception as e:
        print("select stock fail: {}", e)
        return False

    return True


def select_ticker_symbol(driver, ticker_symbol):
    # 股票代码输入框
    ticker_symbol_input_xpath = '//*[@id="main"]/div[2]/div[1]/div[2]/div/div[2]/form/div[2]/div[1]/div/div/div/div/input'

    try:
        ticker_symbol_input = driver.find_element(By.XPATH, ticker_symbol_input_xpath)

        ticker_symbol_input.clear()

        for code in ticker_symbol:
            ticker_symbol_input.send_keys(code)
            time.sleep(operation_interval(0.5))

        time.sleep(operation_interval(1))

        # 选择第一个匹配项
        ticker_symbol_input.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

        time.sleep(operation_interval(1))

    except Exception as e:
        print("select stock fail: {}", e)
        return False

    return True


def selection_sort(driver):
    # 年报选择按钮
    annual_report_xpath = '//*[@id="main"]/div[2]/div[1]/div[2]/div/div[2]/form/div[2]/div[6]/div/span[1]/span'

    try:
        driver.find_element(By.XPATH, annual_report_xpath).click()

        time.sleep(operation_interval(1))

    except Exception as e:
        print("select stock fail: {}", e)
        return False

    return True


def stock_list_get_data(driver, xpath):
    try:
        WebDriverWait(driver, timeout=30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    xpath,
                )
            )
        )

        list = driver.find_element(By.XPATH, xpath).find_elements(By.XPATH, "./*")

        for elem in list:
            download_the_file(
                driver,
                elem.find_element(By.CLASS_NAME, "el-table_1_column_3").find_element(
                    By.TAG_NAME, "a"
                ),
            )

    except Exception as e:
        print("select stock fail: {}", e)
        return False

    return True


def stock_list_flip_page(driver):
    # 下一页
    button_next_xpath = '//*[@id="main"]/div[2]/div[1]/div[1]/div[3]/div/button[2]'
    # 股票列表
    stock_data_list_xpath = (
        '//*[@id="main"]/div[2]/div[1]/div[1]/div[2]/div/div[3]/table/tbody'
    )

    try:
        button_next = driver.find_element(By.XPATH, button_next_xpath)

        while not button_next.get_attribute("disabled"):
            stock_list_get_data(driver, stock_data_list_xpath)

            button_next.click()
            time.sleep(operation_interval(1.5))

        stock_list_get_data(driver, stock_data_list_xpath)

    except Exception as e:
        print("select stock fail: {}", e)
        return False

    return True


def query(driver, ticker_symbol, date):

    select_ticker_symbol(driver, ticker_symbol)

    filter_by_date(driver, date)

    selection_sort(driver)

    stock_list_flip_page(driver)
