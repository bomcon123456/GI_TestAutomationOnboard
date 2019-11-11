from pom.common.base.base_page import BasePage


class AskerProblemPage(BasePage):
    def is_active(self):
        is_on_problem_route = '/problem' in self.browser.driver.current_url
        return is_on_problem_route
