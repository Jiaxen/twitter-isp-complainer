import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import config


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
        print(f"DOWNLOAD SPEED: {str(self.down)}")
        print(f"UPLOAD SPEED: {str(self.up)}")

    def tweet_at_provider(self):
        if self.up < config.PROMISED_UP and self.down < config.PROMISED_UP:
            print("Speeds seem to be unacceptable.")
            print(f"Promised DOWNLOAD SPEED: {config.PROMISED_DOWN}")
            print(f"Promised UPLOAD SPEED: {config.PROMISED_UP}")

            try:
                print("Logging into Twitter...")
                self.driver.get("https://twitter.com/i/flow/login")
                time.sleep(5)

                email = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
                email.send_keys(config.TWITTER_EMAIL)
                next_button = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span')
                next_button.click()
                time.sleep(3)

                password = self.driver.find_element(by=By.NAME, value='password')
                password.send_keys(config.TWITTER_PASSWORD)
                time.sleep(2)
                password.send_keys(Keys.ENTER)

                print("Tweeting complaint...")
                tweet = f'Testing :) -JH'
                tweet_textbox = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
                tweet_textbox.send_keys(tweet)
                time.sleep(2)
                tweet_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
                tweet_button.click()

                print("Tweeted!")

            except NoSuchElementException:
                print("Something went wrong :(")

        else:
            print("Speeds seem to be acceptable.")
