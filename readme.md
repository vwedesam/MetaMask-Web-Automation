
# MetaMask Web Automation

## What this test does
1. install and load Metamask extension
2. setup(import passphrase, enter password) Metamask account
3. turn on test network
4. switch to ropsten network
5. add new network(network name, chainId, rpc url, etc)
6. connect a web3 app to metamask
7. import Custom Token
8. and lot more ...

## Setup
1. create a virtual env
2. add the required env vars
3. download chromedriver (https://chromedriver.chromium.org/downloads)

`chromedriver version should be the same as the chrome installed on your PC `

## RUN

```shell
    py app.py
```

## Environment (virtual env)

```shell
export SITE_URL = ""
export SECRET_RECOVERY_PHRASE = ""
export META_MASK_PASSWORD = ""
export CONTRACT_ADDRESS = ""

```
