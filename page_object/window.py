

class BrowserWindow:

    def __init__(self, driver):
        self.driver = driver
        #  get all available windows
        self.windows = driver.window_handles
        print(self.windows)

    def switch_to_metaMask_window(self):
        metaMask_window_id = self.windows[0]
        self.driver.switch_to.window(metaMask_window_id)

    def switch_to_Main_window(self):
        main_window_id = self.windows[1]
        self.driver.switch_to.window(main_window_id)

    def switch_to_metaMask_PopUp_window(self):
        metaMask_window_id = self.windows[1]
        self.driver.switch_to.window(metaMask_window_id)

    def switch_to_back_to_Main_window_after_metaMask_connect_app_popup_window(self):
        main_window_id = self.windows[0]
        self.driver.switch_to.window(main_window_id)

    def switch_to_metaMask_Switch_Account_PopUp_window(self):
        try:
            metaMask_Switch_Account_PopUp_window_id = self.windows[2]
            self.driver.switch_to.window(metaMask_Switch_Account_PopUp_window_id)
        except:
            pass
