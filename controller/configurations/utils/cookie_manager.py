import pickle

class CookieManager:
    """ Add and remove browser cookies """

    def __init__(self, browser, service_name):
        self.browser = browser
        self.service = service_name
        self.path = f"configurations/utils/cookies/{self.service}.pickle"

    def save_cookies_in_pickle(self):
        """ Store browser cookies in a pickle file """

        with open(self.path, "wb") as file:
            pickle.dump(self.browser.get_cookies(), file)
        print(f'Cookies saved to {self.service}.pickle')

    def add_cookies_to_browser(self):
        """ Restore browser cookies """

        try:
            with open(self.path, "rb") as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    if 'expiry' in cookie:
                        del cookie['expiry']
                    self.browser.add_cookie(cookie)
            print('Cookies loaded into browser successfully')

        except FileNotFoundError as err:
            print(err)
            print('Cookies not added to the browser')
