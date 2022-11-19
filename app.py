import unittest
from selenium import webdriver

from page_object.metaMask_object import MetaMaskClass
from page_object.window import BrowserWindow
from tests.config import metaMask_password, metaMask_recovery_phrase, site_url, contract_address

import os
import time

# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# metamask Extension
PATH = "./chromedriver.exe"
EXTENSION_PATH = './metaMask_extension.crx'
EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'

# ENV
SITE_URL = site_url
SECRET_RECOVERY_PHRASE = metaMask_recovery_phrase
META_MASK_PASSWORD = metaMask_password

# for token import
CONTRACT_ADDRESS = contract_address

# Sepolia Testnet setup
Network_Name = "Sepolia Testnet"
RPC_URL = "https://rpc-sepolia.rockx.com"
ChainID = "11155111"
Symbol = "SEP(ETH)"
Block_Explorer = "https://sepolia.otterscan.io"


class MetaMaskTest(unittest.TestCase):

    def setUp(self):
        opts = webdriver.ChromeOptions()
        opts.add_extension(EXTENSION_PATH)

        self.browser = webdriver.Chrome(executable_path=PATH, options=opts)

        self.window = BrowserWindow(self.browser)

    # @unittest.skip("skipping")
    def test_metaMask_installation_and_setup(self):

        metaMask = MetaMaskClass(self.browser)

        self.window.switch_to_metaMask_window()
        print('switching to metaMask window')

        metaMask.initial_navigation()

        time.sleep(3)

        metaMask.account_setup(SECRET_RECOVERY_PHRASE, META_MASK_PASSWORD)

        metaMask.turn_on_test_network()

        metaMask.switch_metamask_network_to_RopSten()

        metaMask.add_new_network_to_metamask(Network_Name, RPC_URL, ChainID, Symbol, Block_Explorer)

        metaMask.switch_metamask_network_to_Goerli()

        metaMask.import_token(contract_address, "samVwede")

        # close current windows
        metaMask.close_current_active_windows()

        time.sleep(2)

        print('switching to Main window')
        self.window.switch_to_Main_window()

        time.sleep(2)

        print('done with automation test process ....')
        print('good bye ....')
        time.sleep(30)  # seconds

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
