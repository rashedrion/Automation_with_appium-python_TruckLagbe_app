from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_and_click(self, by, value):
        try:
            el = self.wait.until(EC.element_to_be_clickable((by, value)))
            el.click()
            logging.info(f"Clicked element: {value}")
            return el
        except Exception as e:
            logging.error(f"Error clicking element {value}: {e}")
            raise

    def wait_and_send(self, by, value, text):
        try:
            el = self.wait.until(EC.element_to_be_clickable((by, value)))
            el.clear()
            el.send_keys(text)
            logging.info(f"Sent keys '{text}' to element: {value}")
            return el
        except Exception as e:
            logging.error(f"Error sending keys to element {value}: {e}")
            raise

    def wait_for_element(self, by, value):
        try:
            el = self.wait.until(EC.presence_of_element_located((by, value)))
            logging.info(f"Element located: {value}")
            return el
        except Exception as e:
            logging.error(f"Error locating element {value}: {e}")
            raise
