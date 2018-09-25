from twocaptchaapi import TwoCaptchaApi
from credentials import twocaptcha_api_key


class Captcha(object):
    def __init__(self, captcha):
        self.captcha = captcha
        self.api = TwoCaptchaApi(twocaptcha_api_key)

    def solve(self):
        captcha = self.api.solve(self.captcha)
        return captcha.await_result()
