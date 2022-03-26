from twitter_bot import ISPComplainerTwitterBot
import config

if __name__ == '__main__':
    bot = ISPComplainerTwitterBot(config)
    bot.get_internet_speed()
    bot.tweet_at_provider()
