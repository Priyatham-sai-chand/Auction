
from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'auctionimages' # Must be replaced by your <storage_account_name>
    account_key = '3W/fel22r8ExgQMDr8KOxxklp80/slPtAznb+G1Hkq0DWuX2bOIXnQMpgmU/BIJdIWnbDsgMr2SbC5l9qfJJ6g==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

