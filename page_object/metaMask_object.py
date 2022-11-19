from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MetaMaskClass(BasePage):

    def initial_navigation(self):

        welcome_text_selector = '#app-content > div > div.main-container-wrapper > div > div > div > div.welcome-page__header'

        get_started_btn_xpath = '//button[text()="Get Started"]'
        import_wallet_btn_xpath = '//button[text()="Import wallet"]'
        opt_out_btn_xpath = '//button[text()="No Thanks"]'

        # wait for welcome text
        # WebDriverWait(self.browser, 300).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, welcome_text_selector))
        # )
        time.sleep(3)

        # click get started button to continue
        self.browser.find_element(By.XPATH, get_started_btn_xpath).click()

        time.sleep(2)

        # click import existing wallet button
        self.browser.find_element(By.XPATH, import_wallet_btn_xpath).click()

        time.sleep(2)

        # click opt out button
        self.browser.find_element(By.XPATH, opt_out_btn_xpath).click()

    def account_setup(self, SECRET_RECOVERY_PHRASE, PASSWORD):

        # After this you will need to enter you wallet details

        inputs = self.browser.find_elements(By.XPATH, '//input')

        inputs[0].send_keys(SECRET_RECOVERY_PHRASE)
        inputs[1].send_keys(PASSWORD)
        inputs[2].send_keys(PASSWORD)

        time.sleep(2)

        self.browser.find_element(By.CSS_SELECTOR, '.first-time-flow__terms').click()

        time.sleep(2)

        self.browser.find_element(By.XPATH, '//button[text()="Import"]').click()

        # wait for congratulation text
        congrats_selector = '#app-content > div > div.main-container-wrapper > div > div > div.first-time-flow__header'

        # WebDriverWait(self.browser, 300).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, congrats_selector))
        # )
        time.sleep(10)

        self.browser.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/button').click()

        time.sleep(2)
        # close meta mask info modal
        self.browser.find_element(By.CSS_SELECTOR, "#popover-content > div > div > section > header > div > button").click()
        time.sleep(2)

    def load_metaMask_extension(self, EXTENSION_ID):

        # self.browser.execute_script("window.open('');")
        # self.browser.switch_to.window(self.browser.window_handles[0])
        # open popup from main window
        self.browser.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))

    def turn_on_test_network(self):
        # network dropdown
        self.network_dropdown_selector = "#app-content > div > div.app-header.app-header--back-drop > div > div.app-header__account-menu-container > div.app-header__network-component-wrapper > div > span"
        self.browser.find_element(By.CSS_SELECTOR, self.network_dropdown_selector).click()

        time.sleep(2)

        # add all test network
        show_hide_network_link_selector = "#app-content > div > div.menu-droppo-container.network-droppo > div > div.network-dropdown-header > div.network-dropdown-content > span > a"
        self.browser.find_element(By.CSS_SELECTOR, show_hide_network_link_selector).click()

        time.sleep(2)

        # show test networks
        show_test_network_selector = "#app-content > div > div.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div.settings-page__body > div:nth-child(7) > div:nth-child(2) > div > div > div:nth-child(1) > div:nth-child(2) > div"
        self.browser.find_element(By.CSS_SELECTOR, show_test_network_selector).click()

        time.sleep(2)

        # cancel add test network modal
        cancel_modal = "#app-content > div > div.main-container-wrapper > div > div.settings-page__header > div.settings-page__close-button"
        self.browser.find_element(By.CSS_SELECTOR, cancel_modal).click()
        time.sleep(2)

    def switch_metamask_network_to_Goerli(self):
        # network dropdown
        self.browser.find_element(By.CSS_SELECTOR, self.network_dropdown_selector).click()

        time.sleep(2)

        # select Goerli network
        Goerli_selector = "li.dropdown-menu-item:nth-child(4) > span:nth-child(3)"
        self.browser.find_element(By.CSS_SELECTOR, Goerli_selector).click()

        time.sleep(2)

    def switch_metamask_network_to_RopSten(self):
        # network dropdown
        self.browser.find_element(By.CSS_SELECTOR, self.network_dropdown_selector).click()

        time.sleep(2)

        # select ropsten network
        ropsten_selector = "#app-content > div > div.menu-droppo-container.network-droppo > div > div.network-dropdown-list > div > li:nth-child(1)"
        self.browser.find_element(By.CSS_SELECTOR, ropsten_selector).click()

        time.sleep(2)

    def add_new_network_to_metamask(self, Network_Name, RPC_URL, ChainID, Symbol=None, Block_Explorer=None):
        # network dropdown
        self.browser.find_element(By.CSS_SELECTOR, self.network_dropdown_selector).click()

        time.sleep(2)

        # add network button
        add_network_btn_selector = "#app-content > div > div.menu-droppo-container.network-droppo > div > button"
        self.browser.find_element(By.CSS_SELECTOR, add_network_btn_selector).click()

        time.sleep(2)

        # network Name
        network_name_input_selector = "#app-content > div > div.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div > div.networks-tab__content > div > div.networks-tab__add-network-form-body > div:nth-child(1) > label > input"
        self.browser.find_element(By.CSS_SELECTOR, network_name_input_selector).send_keys(Network_Name)

        # chain id
        chain_id_input_selector = "#app-content > div > div.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div > div.networks-tab__content > div > div.networks-tab__add-network-form-body > div:nth-child(3) > label > input"
        self.browser.find_element(By.CSS_SELECTOR, chain_id_input_selector).send_keys(ChainID)

        # RPC URL
        RPC_URL_input_selector = "#app-content > div > div.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div > div.networks-tab__content > div > div.networks-tab__add-network-form-body > div:nth-child(2) > label > input"
        self.browser.find_element(By.CSS_SELECTOR, RPC_URL_input_selector).send_keys(RPC_URL)

        # Currency Symbol
        if Symbol:
            symbol_input_selector = "#app-content > div > div.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div > div.networks-tab__content > div > div.networks-tab__add-network-form-body > div:nth-child(4) > label > input"
            self.browser.find_element(By.CSS_SELECTOR, symbol_input_selector).send_keys(Symbol)

        # Block Explorer
        if Block_Explorer:
            block_explorer_input_selector = "#app-content > div > div.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div > div.networks-tab__content > div > div.networks-tab__add-network-form-body > div:nth-child(5) > label > input"
            self.browser.find_element(By.CSS_SELECTOR, block_explorer_input_selector).send_keys(Block_Explorer)

        try:
            # save
            time.sleep(2)

            save_network_btn_selector = "#app-content > div > div.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div > div.networks-tab__content > div > div.networks-tab__add-network-form-footer > button.button.btn--rounded.btn-primary"
            self.browser.find_element(By.CSS_SELECTOR, save_network_btn_selector).click()
        except:
            pass

        time.sleep(3)

    def import_token(self, contract_address, symbol, decimal=18):
        # my Account dropdown
        import_token_link_selector = ".button"
        self.browser.find_element(By.CSS_SELECTOR, import_token_link_selector).click()

        time.sleep(2)

        contract_address_input_selector = "#custom-address"
        self.browser.find_element(By.CSS_SELECTOR, contract_address_input_selector).send_keys(contract_address)

        time.sleep(5)

        symbol_input_selector = "#custom-symbol"
        self.browser.find_element(By.CSS_SELECTOR, symbol_input_selector).send_keys(str(symbol))

        decimal_input_selector = "#custom-decimals"
        decimal_input = self.browser.find_element(By.CSS_SELECTOR, decimal_input_selector)
        decimal_input.send_keys(Keys.BACKSPACE) # clear input field with back space
        decimal_input.send_keys(decimal)

        time.sleep(3)

        add_token_btn_selector = "button.button"
        self.browser.find_element(By.CSS_SELECTOR, add_token_btn_selector).click()

        time.sleep(2)

        import_token_btn_selector = "#app-content > div > div.main-container-wrapper > div > div.page-container__footer > footer > button.button.btn--rounded.btn-primary.btn--large.page-container__footer-button"
        self.browser.find_element(By.CSS_SELECTOR, import_token_btn_selector).click()

        time.sleep(2)

    def connect_app_with_metamask(self):

        try:
            time.sleep(2)

            # next button
            next_btn_selector = "#app-content > div > div.main-container-wrapper > div > div.permissions-connect-choose-account > div.permissions-connect-choose-account__footer-container > div.permissions-connect-choose-account__bottom-buttons > button.button.btn--rounded.btn-primary"
            self.browser.find_element(By.CSS_SELECTOR, next_btn_selector).click()

            time.sleep(2)

            # confirm button
            confirm_btn_selector = "#app-content > div > div.main-container-wrapper > div > div.page-container.permission-approval-container > div.permission-approval-container__footers > div.page-container__footer > footer > button.button.btn--rounded.btn-primary.page-container__footer-button"
            self.browser.find_element(By.CSS_SELECTOR, confirm_btn_selector).click()

        except Exception as e:
            print(e)
            print('error while interacting with metamask notification window ')
            pass

    def confirm_Trx(self):

        try:
            time.sleep(4)
            # confirm transaction button
            confirm_btn_selector = "button.button:nth-child(2)"
            self.browser.find_element(By.CSS_SELECTOR, confirm_btn_selector).click()

        except:
            print('error while interacting with metamask notification window ')
            pass

    def close_current_active_windows(self):
        time.sleep(2)
        self.browser.close()

