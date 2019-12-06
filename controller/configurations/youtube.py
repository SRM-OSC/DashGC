from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import traceback as tb

class YouTube:
    ''' YouTube configuration '''

    def __init__(self):
        self.browser = None
        self.path = "C:\\Program Files (x86)\\Google\\Chrome\\chromedriver.exe"

    def launch_youtube(self):
        ''' Launch www.youtube.com '''

        self.browser = webdriver.Chrome(self.path)
        self.browser.maximize_window()
        self.browser.get('https://www.youtube.com')

        return 1

    def load_first_video(self):
        ''' Load the first video that is present '''

        css = 'a#video-title-link.yt-simple-endpoint.style-scope.ytd-rich-grid-video-renderer'

        first_video = self.browser.find_element_by_css_selector(css)
        first_video.click() # click may get blocked by an overlaying element

        return 1

    def pause_video(self):
        ''' Pause the video that is currently being played '''

        css = 'button.ytp-play-button.ytp-button'

        pause_button = self.browser.find_element_by_css_selector(css)
        pause_button.send_keys(Keys.SPACE)  # [SPACE] won't be blocked

        return 1

    def resume_video(self):
        ''' Resume the paused video '''

        self.pause_video()  # just hit the play button again

        return 1

    def close_youtube(self):
        ''' Close youtube.com '''

        self.browser.quit() # terminate the browser instance

        return 0

    def execute_command_for_gesture(self, gesture_code):
        ''' Execute action for the given gesture code '''

        gesture_map = { "1": self.launch_youtube,
            "2": self.load_first_video,
            "3": self.pause_video,
            "4": self.resume_video,
            "5": self.close_youtube
        }

        try:
            return (gesture_map[gesture_code])()

        except:
            print(tb.format_exc())
            return -1
