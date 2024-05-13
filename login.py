from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

target_url = "http://www.cninfo.com.cn/new/commonUrl/pageOfSearch?url=disclosure/list/search&lastPage=index"


def get_window(driver):
    driver.get(target_url)

    try:
        # 等待查询界面加载完毕
        WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="main"]/div[2]/div[1]/div[2]/div/div[2]/div[1]/button',
                )
            )
        )
    except Exception:
        return False

    return True


def login(driver):
    if not get_window(driver):
        print("[main] try Enter the inquiry page fail")
