from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from booking import constants as cons
from booking.booking_filtration import BookingFiltration
from time import sleep


class Booking(webdriver.Chrome):
    def __int__(self):
        # self.service = Service(executable_path=ChromeDriverManager().install())
        self.service = Service(executable_path="cons.Executable_Path")
        self.driver = webdriver.Chrome(service=self.service)
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if cons.teardown:
            self.quit()

    def choose_travel_type(self):
        travel_type = self.find_element(By.XPATH, "//*[@aria-label='Search for flights ']")
        travel_type.click()
        sleep(3)

    def land_first_page(self):
        self.implicitly_wait(15)
        self.maximize_window()
        # self.get(cons.BASE_URL)
        self.get(cons.BASE_URL_FLIGHT)

    def change_currency(self, currency=None):
        self.find_element(By.XPATH,
                          "//button/span[@class='chXn-trigger-icon']").click()
        self.find_element(By.XPATH,
                          f"//*[@class='chXn-content-all-currencies']//"
                          f"button[@class='chXn-item']/span[text()='{currency}']").click()
        self.find_element(By.XPATH, "//*[@class='Iqt3-button-content' and text()='This visit only']").click()

    def select_source(self, place_from):
        sleep(3)
        search_field = self.find_element(By.XPATH, "//input[@aria-label='Flight origin input']")
        search_field.send_keys(Keys.BACKSPACE)
        search_field.send_keys(Keys.BACKSPACE)
        search_field.send_keys(place_from)
        second_result = self.find_element(By.XPATH, "//*[@id='flight-origin-smarty-input-list']/li[2]")
        second_result.click()

    def destination_place(self, place_destination):
        search_field = self.find_element(By.XPATH, "//*[@aria-label='Flight destination input']")
        search_field.send_keys(place_destination)
        select_destination = self.find_element(By.XPATH, "//li[1][@role='option']")
        select_destination.click()

    def choosing_dates(self, check_in_date, check_out_date):
        self.find_element(
            By.XPATH, "//*[@class='sR_k-input sR_k-mod-responsive']").click()
        self.find_element(
            By.XPATH, f"//div[@class='ATGJ-monthWrapper']/div[1]/div[2]/*[@aria-label='{check_in_date}']").click()
        self.find_element(
            By.XPATH,
            "//div[@class='sR_k sR_k-mod-size-mcfly sR_k-mod-radius-base sR_k-pres-mcfly"
            " sR_k-mod-variant-inline sR_k-mod-responsive']/div[2]").click()
        self.find_element(
            By.XPATH, f"//div[@class='ATGJ-monthWrapper']/div[2]/div[2]/*[@aria-label='{check_out_date}']").click()
        # end_date.click()

    def adults_number(self, count):
        self.find_element(By.XPATH, "//*[@class='zcIg']/div[2]").click()
        while True:
            self.find_element(
                By.XPATH, "//div[1][@class='u9Xa']//button[@aria-label='Decrement']").click()
            adults_count = self.find_element(
                By.XPATH, "//div[1][@class='u9Xa']//input[@aria-label='Adults']").get_attribute('aria-valuenow')
            if int(adults_count) == 1:
                break

        increase_adults = self.find_element(
            By.XPATH, "//div[1][@class='u9Xa']//button[@aria-label='Increment']")
        for i in range(count-1):
            increase_adults.click()

    def click_search(self):
        search_button = self.find_element(By.XPATH, "//*[@type='submit' and @aria-label='Search']")
        search_button.click()
        sleep(3)

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.lowest_price_flight()
        filtration.apply_start_rating(3,4,5)

    def report_results(self):
        flight_lists = self.driver.find_elements(By.CLASS_NAME, "nrc6")
