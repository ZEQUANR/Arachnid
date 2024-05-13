import os
from selenium import webdriver

from login import login
from query import query


def init_firefox(path):
    download_path = os.path.join(os.getcwd(), "downloads\\" + path)

    if not os.path.exists(download_path):
        os.makedirs(download_path, 0o755)

    profile = webdriver.FirefoxProfile()
    file_type = (
        "application/octet-stream , application/zip, application/kswps,application/pdf"
    )

    profile.set_preference("browser.link.open_newwindow", 3)
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.dir", download_path)
    profile.set_preference("browser.download.downloadDir", download_path)
    profile.set_preference("browser.download.defaultFolder", download_path)
    profile.set_preference("borwser.download.manager.showWhenStaring", False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", file_type)

    options = webdriver.FirefoxOptions()
    options.profile = profile

    return webdriver.Firefox(options)


if __name__ == "__main__":

    for code in ["000002", "000004"]:
        driver = init_firefox(code)
        try:
            login(driver)

            query(driver, code, "2010-01-01")

        except Exception as e:
            print(e)

        driver.quit()
