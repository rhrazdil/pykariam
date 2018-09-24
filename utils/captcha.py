from twocaptchaapi import TwoCaptchaApi
from credentials import twocaptcha_api_key


class Captcha(object):
    def __init__(self, captcha_png):
        self.captcha_png = captcha_png
        self.api = TwoCaptchaApi(twocaptcha_api_key)

    def solve(self):
        captcha = self.api.solve(self.captcha_png)
        return captcha.await_result()
