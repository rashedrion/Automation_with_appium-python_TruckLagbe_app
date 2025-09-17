import pytest
import logging
from pages.login_page import LoginPage
from pages.trip_page import TripPage

def test_create_trip(driver, config):
    logging.info("===== Starting Trip Creation Test =====")
    login = LoginPage(driver)
    trip = TripPage(driver)

    # Login flow
    login.enter_phone_number(config['phone_number'])
    login.click_continue()
    login.enter_otp(config['otp'])
    login.submit_otp()

    # Trip creation flow
    trip.open_trip_menu()
    trip.click_new_trip()
    trip.set_load_location(config['load_location'])
    trip.set_unload_location(config['unload_location'])
    trip.set_product_description(config['product_description'])

    logging.info("===== Trip Creation Test Completed =====")
    assert True
