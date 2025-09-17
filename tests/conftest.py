import pytest
import yaml
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os

@pytest.fixture(scope="session")
def config():
    config_path = os.path.join(os.path.dirname(__file__), "../config/config.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def driver(config):
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "app": os.path.abspath(os.path.join(os.path.dirname(__file__), "../trucklagbe.apk")),
        "automationName": "UiAutomator2",
        "appium:deviceName": "Android Emulator",
        "appium:noReset": False
    })
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    yield driver
    driver.quit()
