from time import sleep

from selenium.webdriver.common.by import By
# from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_start_rating(self, *star_values):
        self.driver.find_element(By.XPATH, "//*[text()='Flight quality']").click()
        sleep(2)
        flight_quality = self.driver.find_elements(
            By.XPATH, "//*[@aria-label='Flight quality']//span[@class='PVIO-input-wrapper']//input")
        element=1
        for fq in flight_quality:
            if fq.get_attribute("aria-checked") == "false":
                element = element + 1
                continue
            else:
                fq.find_element(
                    By.XPATH,
                    f"//div[@aria-label='Flight quality']/*[@class='Qk4D Qk4D-mod-theme-no-border Qk4D-mod-variant-no-spacing'][{element}]").click()
            element = element + 1
        for star in star_values:
            fq.find_element(
                By.XPATH,
                f"//div[@aria-label='Flight quality']/*[@class='Qk4D Qk4D-mod-theme-no-border Qk4D-mod-variant-no-spacing'][{star}]").click()
            sleep(2)

    def lowest_price_flight(self):
        cheapest = self.driver.find_element(By.XPATH, "//div[@class='Hv20-content' and @data-content='price_a']")
        cheapest.click()
        sleep(3)

