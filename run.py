import sys

from app.screenshot_comparator import compare_screenshots
from app.webdriver import Driver


class Run(Driver):

    def __init__(self, env):
        super().__init__(env=env)

    def run(self):
        try:
            app_code = self.env["app_code"]
            reference_screenshot_name = app_code + "_reference_screen.png"
            actual_screenshot_name = app_code + "_actual_screen.png"
            result_screenshot_name = app_code + "_result_screen.png"

            self.get_page(self.env["app_url"])
            print("Screenshot captured as {}...".format(actual_screenshot_name))
            self.make_screenshot(actual_screenshot_name)
            print("Screenshot comparision started...")
            compare_screenshots(reference_screenshot_name, actual_screenshot_name, result_screenshot_name)
        finally:
            self.clean_up()


if __name__ == '__main__':
    env = sys.argv[1]
    Run(env=env).run()
