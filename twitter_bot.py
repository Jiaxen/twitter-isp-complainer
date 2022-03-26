from selenium import webdriver


class ISPComplainerTwitterBot:
    def __init__(self, config):
        self.driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass
