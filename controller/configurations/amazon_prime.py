from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import traceback as tb
import utils.cookie_manager as cm

class AmazonPrimeVideo:
    ''' Amazon Prime Video configuration '''

    def __init__(self):
        self.browser = None
        self.path = "C:\\Program Files (x86)\\Google\\Chrome\\chromedriver.exe"
        self.username = ''
        self.password = ''
        self.save_cookies_on_exit = True

    def launch_amazon_prime(self, fresh_start=False):
        ''' Launch amazon prime login window '''

        self.browser = webdriver.Chrome(self.path)  # open a browser window
        self.browser.maximize_window()              # maximize it

        self.browser.get('https://www.primevideo.com/') # load primevideo.com

        if not fresh_start: # if this is not a fresh start

            # then add cookies in the browser
            cookie_manager = cm.CookieManager(self.browser, "amazon_prime")
            cookie_manager.add_cookies_to_browser()
            del cookie_manager
            # refresh page
            self.browser.get('https://www.primevideo.com/')

        else:   # otherwise go to the sign in page

            sign_in_button_css = 'a._33ixDQ'
            sign_in = self.browser.find_element_by_css_selector(sign_in_button_css)
            sign_in.click()

        return 1

    def login_to_amazon_prime(self):
        ''' Login to amazon prime with your credentials '''

        user_css = 'input#ap_email.a-input-text.a-span12.auth-autofocus.auth-required-field'
        pass_css = 'input#ap_password.a-input-text.a-span12.auth-required-field'
        sign_in_button_css = 'input#signInSubmit.a-button-input'

        user = self.browser.find_element_by_css_selector(user_css)
        pswd = self.browser.find_element_by_css_selector(pass_css)
        sign = self.browser.find_element_by_css_selector(sign_in_button_css)

        user.send_keys(self.username)   # enter username
        pswd.send_keys(self.password)   # enter password
        sign.click()                    # click the sign in button

        return 1

    def resume_last_show(self):
        ''' Resume watching the last show that you were watching '''

        pass    # waiting for valid credentials

    def close_amazon_prime(self):
        ''' Close primevideo.com '''

        if self.save_cookies_on_exit:
            cookie_manager = cm.CookieManager(self.browser, "amazon_prime")
            cookie_manager.save_cookies_in_pickle()
            del cookie_manager

        self.browser.quit() # terminate the browser instance

        return 0

    def execute_command_for_gesture(self, gesture_code):
        ''' Execute action for the given gesture code '''

        gesture_map = { "1": [self.launch_amazon_prime, ()],
            "2": [self.launch_amazon_prime, (True, )],
            "3": [self.login_to_amazon_prime, ()],
            "4": [self.resume_last_show, ()],
            "5": [self.close_amazon_prime, ()]
        }

        try:
            func, args = gesture_map[gesture_code]
            return func(*args)
        except:
            self.save_cookies_on_exit = False
            print(tb.format_exc())
            return -1
