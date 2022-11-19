import os

metaMask_password = os.getenv('META_MASK_PASSWORD')
metaMask_recovery_phrase = os.getenv('SECRET_RECOVERY_PHRASE')

site_url = os.getenv('SITE_URL') or "http://localhost:3000"

contract_address = os.getenv('CONTRACT_ADDRESS')

