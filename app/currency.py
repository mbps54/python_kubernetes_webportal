import requests
import json
import os

def get_rates():
    response = requests.get("http://api.currencylayer.com/live?access_key=ca0cdd8c332da1840ec1e46a16ece708&source=USD&currencies=RUB,TRY&format=1")
    usdrub = ((response.json())['quotes'])['USDRUB']
    usdtry = ((response.json())['quotes'])['USDTRY']
    try:
        os.makedirs(os.path.expanduser("../temp"))
    except:
        pass
    text_file = open('../temp/rates.yaml', "w")
    n = text_file.write(f"---\n'usdrub': {usdrub}\n")
    n = text_file.write(f"'usdtry': {usdtry}\n...")
    text_file.close()

if __name__ == "__main__":
    get_rates()