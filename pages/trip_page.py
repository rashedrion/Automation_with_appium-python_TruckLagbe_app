from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class TripPage(BasePage):
    def open_trip_menu(self):
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.view.ViewGroup").instance(58)')

    def click_new_trip(self):
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.view.ViewGroup").instance(45)')

    def set_load_location(self, location):
        self.wait_and_send(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("লোড লোকেশন")', location)
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{location}")')

    def set_unload_location(self, location):
        self.wait_and_send(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("আনলোড লোকেশন")', location)
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{location}")')

    def set_product_description(self, description):
        desc_box = self.wait_for_element(AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(1)')
        desc_box.send_keys(description)
