# twitter-isp-complainer
Does your internet service provider under-deliver?

This script will check your internet speed and tweet your service provider a complaint when it is not holding up its end of the bargain!

Similar to https://github.com/james-atkinson/speedcomplainer but using Selenium to interact with www.speedtest.net and www.twitter.com, as opposed to the speedtest cli and the twitter api.

## How to use
- Download a [Chrome driver](https://chromedriver.chromium.org/downloads).

- Modify the config file with your details.

- Run ```python main.py``` or use a scheduler