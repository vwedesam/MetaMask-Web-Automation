

class BasePage(object):
    """
    class to initialize the base page
    """

    def __init__(self, driver):
        self.browser = driver
        self.login_elem = ''
        self.income_elem = ''
        self.header_text = ''
        self.elem = ''
        self.action_button = ''
        self.elem_value = ''
        self.network_dropdown_selector = ''
