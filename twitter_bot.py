import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ISPComplainerTwitterBot:
    def __init__(self, config):
        self.driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH, chrome_options=config.chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        print("STARTING SPEED TEST")
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)

        # Accept cookies
        try:
            accept_button = self.driver.find_element(by=By.ID, value="_evidon-banner-acceptbutton")
            accept_button.click()
        except NoSuchElementException:
            print('Could not accept cookies')
        time.sleep(3)

        # Press Go button
        test_speed_button = self.driver.find_element(by=By.CLASS_NAME, value="start-text")
        test_speed_button.click()

        # Wait for test results
        in_progress = True
        while in_progress:
            progress = self.driver.find_element(by=By.CLASS_NAME, value="overall-progress").text
            if progress.startswith("Your speed test has completed"):
                in_progress = False
            else:
                time.sleep(5)

        # Get results
        self.up = float(self.driver.find_element(by=By.CLASS_NAME, value="upload-speed").text)
        self.down = float(self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text)

        print("TEST RESULTS: ")
        print("DOWNLOAD SPEED: ", str(self.down))
        print("UPLOAD SPEED: ", str(self.up))


    def tweet_at_provider(self):
        pass
