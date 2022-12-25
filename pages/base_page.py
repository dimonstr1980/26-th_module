from urllib.parse import urlparse


class BasePage(object):
    # конструктор класса — специальный метод с ключевым словом __init__
    # нам нужны объект веб-драйвера, вэб-адрес страницы и время ожидания элементов.
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path


class BaseElement(object):

    def __init__(self, driver, locator):
        print(locator)
        self.e = driver.find_element(*locator)
