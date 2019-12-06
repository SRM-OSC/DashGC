from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import traceback as tb
import utils.cookie_manager as cm


class Netflix:
    """ Netflix configuration """

    def __init__(self):
        self.actions = None
        self.browser = None
        self.path = "C:\\Program Files (x86)\\Google\\Chrome\\chromedriver.exe"
        self.username = ''
        self.password = ''
        self.account = ''
        self.save_cookies_on_exit = True

    def launch_netflix(self, fresh_start=False):
        """ Launch netflix login window """

        self.browser = webdriver.Chrome(self.path)
        self.browser.maximize_window()

        self.browser.get('https://www.netflix.com/in/login')

        if not fresh_start: # if this is not a fresh start
            # load cookies in the browser
            cookie_manager = cm.CookieManager(self.browser, "netflix")
            cookie_manager.add_cookies_to_browser()
            del cookie_manager
            # refresh page
            self.browser.get('https://www.netflix.com/in/login')

        return 1

    def login_to_netflix(self):
        """ Login to netflix with your credentials """

        user_css = 'input#id_userLoginId.nfTextField'
        pass_css = 'input#id_password.nfTextField'
        sign_in_button_css = 'button.btn.login-button.btn-submit.btn-small'
        remember_me_box_css = 'input#bxid_rememberMe_true'

        user = self.browser.find_element_by_css_selector(user_css)
        pswd = self.browser.find_element_by_css_selector(pass_css)
        sign = self.browser.find_element_by_css_selector(sign_in_button_css)
        remb = self.browser.find_element_by_css_selector(remember_me_box_css)

        user.send_keys(self.username)   # enter username
        pswd.send_keys(self.password)   # enter password
        remb.send_keys(Keys.SPACE)      # uncheck the remember me box
        sign.send_keys(Keys.SPACE)      # click the sign in button

        return 1

    def select_account(self):
        """ Select account """

        account_css = f"//a/span[contains(text(), '{self.account}')]"
        account_button = self.browser.find_element_by_xpath(account_css)
        account_button.click()

        return 1

    def resume_last_show(self):
        """ Resume watching the last show that you were watching """

        # find the last show div using xpath
        last_show_xpath = '//div[@data-list-context="continueWatching"]'
        last_show_xpath += '/div/div/div/div/div/div/div/div/div'

        # keep scrolling down until that element is found
        while True:
            try:
                last_show = self.browser.find_element_by_xpath(last_show_xpath)
                break
            except NoSuchElementException:
                js_scroll = "window.scrollTo(0, document.body.scrollHeight);"
                self.browser.execute_script(js_scroll)

        # scroll to the element and click on it to make the resume button visible
        self.actions = ActionChains(self.browser)
        self.actions.move_to_element(last_show).click().perform()

        # extract show playback link from resume button
        resume_button_xpath = "//a[@class=' playLink']"
        resume_button = self.browser.find_element_by_xpath(resume_button_xpath)
        last_show_link = resume_button.get_attribute("href")

        self.browser.get(last_show_link)    # load the last show

        return 1

    def close_netflix(self):
        """ Close netflix.com """

        if self.save_cookies_on_exit:
            cookie_manager = cm.CookieManager(self.browser, "netflix")
            cookie_manager.save_cookies_in_pickle()
            del cookie_manager

        self.browser.quit() # terminate the browser instance

        return 0

    def execute_command_for_gesture(self, gesture_code):
        """ Execute action for the given gesture code """

        gesture_map = { "1": [self.launch_netflix, ()],
            "2": [self.launch_netflix, (True,)],
            "3": [self.login_to_netflix, ()],
            "4": [self.select_account, ()],
            "5": [self.resume_last_show, ()],
            "6": [self.close_netflix, ()]
        }

        try:
            func, args = gesture_map[gesture_code]
            return func(*args)
        except:
            self.save_cookies_on_exit = False
            print(tb.format_exc())
            return -1
