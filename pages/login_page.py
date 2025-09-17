from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class LoginPage(BasePage):
    def enter_phone_number(self, phone):
        self.wait_and_send(AppiumBy.CLASS_NAME, "android.widget.EditText", phone)

    def click_continue(self):
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.view.ViewGroup").instance(45)')

    def enter_otp(self, otp):
        otp_box = self.wait_for_element(AppiumBy.XPATH,
            "//android.widget.FrameLayout[@resource-id='android:id/content']//android.widget.EditText[1]")
        otp_box.send_keys(otp)

    def submit_otp(self):
        self.wait_and_click(AppiumBy.ID, "android:id/text1")
